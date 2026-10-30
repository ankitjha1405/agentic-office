#!/usr/bin/env python3
"""Mirror workspace/jira task files to a real Jira Cloud project.

Commands:
  check        verify credentials and project, list issue types and statuses
  setup        add Blocked and In Review stages to the project workflow and board
  sync [FILE]  push new/changed task files (all changed ones if no FILE)
  hook         same as sync, but never fails; called by Claude Code hooks
  pull         copy new human comments from Jira issues into the task logs

Config (env or .env in the office root): JIRA_SITE, JIRA_EMAIL, JIRA_API_TOKEN, JIRA_PROJECT_KEY.
JIRA_DRY_RUN=1 prints API calls instead of sending them.
"""
import base64, json, os, re, sys, urllib.error, urllib.request, uuid
from datetime import datetime

from common import BOT, JIRA, ROOT, SSL, load_env, parse, roster, task_files, who, describe

STATE = os.environ.get("JIRA_STATE") or os.path.join(JIRA, ".jira-state.json")
LOG = os.path.join(JIRA, ".jira-sync.log")
DEPTS = {"OPS": "ops", "PROD": "product", "DES": "design", "ENG": "engineering", "MKT": "marketing",
         "SALES": "sales", "CS": "customer-success", "RISK": "risk-legal", "HR": "people"}
# Office category -> Jira status names to try, in order (team- and company-managed defaults differ).
TARGETS = {"Not Started": ["To Do", "Backlog", "Open"], "Active": ["In Progress"],
           "Blocked": ["Blocked", "In Progress"], "In Review": ["In Review", "Review", "In Progress"],
           "Complete": ["Done", "Closed", "Resolved"]}
TYPES = {"bug": "Bug", "story": "Story", "epic": "Epic"}


def call(method, path, body=None, base="/rest/api/3"):
    if os.environ.get("JIRA_DRY_RUN"):
        print(method, path, json.dumps(body)[:120] if body else "")
        return {"key": "DRY-1", "transitions": [], "comments": []}
    auth = base64.b64encode(f"{os.environ['JIRA_EMAIL']}:{os.environ['JIRA_API_TOKEN']}".encode()).decode()
    req = urllib.request.Request(os.environ["JIRA_SITE"].rstrip("/") + base + path, method=method,
                                 data=json.dumps(body).encode() if body is not None else None,
                                 headers={"Authorization": "Basic " + auth, "Accept": "application/json",
                                          "Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=20, context=SSL) as r:
            raw = r.read()
            return json.loads(raw) if raw else {}
    except urllib.error.HTTPError as e:
        raise RuntimeError(f"{method} {path} -> {e.code}: {e.read()[:300].decode(errors='replace')}")


def adf(text):
    """Markdown-ish text -> Atlassian Document Format (headings + one paragraph per line)."""
    nodes = []
    for line in text.splitlines():
        if not line.strip():
            continue
        m = re.match(r"(#{1,6}) (.*)", line)
        if m:
            nodes.append({"type": "heading", "attrs": {"level": 3}, "content": [{"type": "text", "text": m.group(2)}]})
        else:
            nodes.append({"type": "paragraph", "content": [{"type": "text", "text": line.replace("**", "")}]})
    return {"type": "doc", "version": 1, "content": nodes or [{"type": "paragraph", "content": []}]}


def plain(node):
    if node.get("type") == "text":
        return node.get("text", "")
    sep = "\n" if node.get("type") in ("doc",) else ""
    return sep.join(plain(c) for c in node.get("content", []))


def load_state():
    try:
        return json.load(open(STATE, encoding="utf-8"))
    except (OSError, ValueError):
        return {"issues": {}}


def save_state(s):
    json.dump(s, open(STATE, "w", encoding="utf-8"), indent=1)


def comment(issue, text):
    call("POST", f"/issue/{issue}/comment", {"body": adf(f"{BOT} {text}"[:30000])})


READY = {"Ready", "Prioritized", "Brief Approved", "Approved", "Qualified", "Triaged"}  # dept statuses meaning "picked, not started"


def transition(issue, category, status=""):
    available = call("GET", f"/issue/{issue}/transitions")["transitions"]
    first = ["Selected for Development"] if category == "Not Started" and status in READY else []
    for name in first + TARGETS[category]:
        for t in available:
            if t["to"]["name"].lower() == name.lower():
                call("POST", f"/issue/{issue}/transitions", {"transition": {"id": t["id"]}})
                return t["to"]["name"]
    return None


def sync_file(path, s, names):
    meta, sections, entries, digest = parse(path)
    key = meta["key"]
    issue = s["issues"].get(key)
    if issue and issue.get("hash") == digest:
        return
    cat = meta.get("category") if meta.get("category") in TARGETS else "Not Started"
    labels = ["office", "office-" + key, DEPTS.get(key.split("-")[0], "company")]
    labels += [p for p in [meta.get("priority")] if p] + (["blocked"] if cat == "Blocked" else [])
    fields = {"summary": f"[{key}] {meta.get('title', '')}"[:250], "labels": labels,
              "description": adf(describe(meta, sections, path, names) + f"\n**Due:** {meta.get('due') or 'none'}")}
    if not issue:
        fields |= {"project": {"key": os.environ["JIRA_PROJECT_KEY"]},
                   "issuetype": {"name": TYPES.get(meta.get("type"), "Task")}}
        try:
            created = call("POST", "/issue", {"fields": fields})
        except RuntimeError:  # project may not have Story/Bug/Epic: fall back to Task
            fields["issuetype"] = {"name": "Task"}
            created = call("POST", "/issue", {"fields": fields})
        # save before any follow-up call can fail, so a rerun updates this issue instead of creating another
        issue = s["issues"][key] = {"key": created["key"], "log": 0, "category": "Not Started",
                                    "status": meta.get("status"), "owner": meta.get("owner")}
        save_state(s)
        comment(issue["key"], f"Ticket created by {who(meta.get('reporter'), names)}. Owner: {who(meta.get('owner'), names)}. Status: {meta.get('status')}.")
        if cat != "Not Started":
            transition(issue["key"], cat, meta.get("status", ""))
            issue["category"] = cat
            save_state(s)
    else:
        call("PUT", f"/issue/{issue['key']}", {"fields": fields})
        if issue.get("category") != cat:
            landed = transition(issue["key"], cat, meta.get("status", ""))
            comment(issue["key"], f"Moved {issue.get('category')} → {cat} (status: {meta.get('status')}"
                                  + (f"; Jira status: {landed})." if landed else "; no matching Jira transition)."))
        elif issue.get("status") != meta.get("status"):
            comment(issue["key"], f"Status changed {issue.get('status')} → {meta.get('status')}.")
        if issue.get("owner") != meta.get("owner"):
            comment(issue["key"], f"Owner changed {who(issue.get('owner'), names)} → {who(meta.get('owner'), names)}.")
    for entry in entries[issue["log"]:]:
        comment(issue["key"], entry)
        issue["log"] += 1
        save_state(s)
    issue.update(log=len(entries), hash=digest, category=cat, status=meta.get("status"), owner=meta.get("owner"))
    save_state(s)


def sync(files, s):
    names = roster()
    for f in files or task_files():
        sync_file(os.path.abspath(f), s, names)


def pull(s):
    """Append human Jira comments to the task log so agents see them."""
    for f in task_files():
        meta, _, _, _ = parse(f)
        issue = s["issues"].get(meta.get("key"))
        if not issue:
            continue
        seen = set(issue.get("seen", []))
        new = [c for c in call("GET", f"/issue/{issue['key']}/comment?orderBy=created")["comments"]
               if c["id"] not in seen and not plain(c["body"]).startswith(BOT)]
        if not new:
            continue
        with open(f, "a", encoding="utf-8") as fh:
            for c in new:
                author = c.get("author", {}).get("displayName", "Jira user")
                text = " ".join(plain(c["body"]).split())
                fh.write(f"- {c['created'][:10]} · {author} (Jira comment on {issue['key']}): {text}\n")
                print(f"{meta['key']} ({issue['key']}): {author}: {text[:80]}")
        # Mark pulled lines as synced so they are not echoed back as bot comments.
        _, _, entries, digest = parse(f)
        issue.update(log=len(entries), hash=digest, seen=sorted(seen | {c["id"] for c in new}))
    save_state(s)


def check():
    me = call("GET", "/myself")
    print("Signed in as", me.get("displayName"), me.get("emailAddress", ""))
    p = call("GET", f"/project/{os.environ['JIRA_PROJECT_KEY']}")
    print("Project", p["key"], "-", p["name"], "| issue types:", ", ".join(t["name"] for t in p.get("issueTypes", [])))
    statuses = {st["name"] for t in call("GET", f"/project/{p['key']}/statuses") for st in t["statuses"]}
    print("Statuses:", ", ".join(sorted(statuses)))


NEW_STAGES = [("Blocked", "Work cannot continue until a blocker is removed."),
              ("In Review", "Work is done and waiting for review or QA.")]
MANUAL = ("Add them by hand instead: Jira project -> Board -> ... -> Configure board -> Columns -> "
          "add columns 'Blocked' and 'In Review' before 'Done'.")


def setup():
    """Add Blocked and In Review to the project's workflow and board (company-managed projects)."""
    key = os.environ["JIRA_PROJECT_KEY"]
    project = call("GET", f"/project/{key}")
    scheme = call("GET", f"/workflowscheme/project?projectId={project['id']}")["values"][0]["workflowScheme"]
    data = call("POST", "/workflows?expand=values.transitions", {"workflowNames": [scheme["defaultWorkflow"]]})
    wf = data["workflows"][0]
    have = {st["name"] for st in data["statuses"]}
    missing = [(n, d) for n, d in NEW_STAGES if n not in have]
    if missing:
        if not wf.get("isEditable", True):
            sys.exit("This project's workflow can't be edited through the API. " + MANUAL)
        defs = [{k: st[k] for k in ("id", "statusReference", "name", "statusCategory", "description")} for st in data["statuses"]]
        next_id = max(int(t["id"]) for t in wf["transitions"]) + 10
        for name, desc in missing:
            ref = str(uuid.uuid4())
            defs.append({"statusReference": ref, "name": name, "statusCategory": "IN_PROGRESS", "description": desc})
            wf["statuses"].append({"statusReference": ref, "layout": {}, "properties": {}, "deprecated": False})
            wf["transitions"].append({"id": str(next_id), "type": "GLOBAL", "toStatusReference": ref, "links": [], "name": name,
                                      "description": "", "validators": [], "triggers": [], "properties": {},
                                      "actions": [{"ruleKey": "system:update-field",
                                                   "parameters": {"field": "resolution", "value": "", "mode": ""}}]})
            next_id += 10
        call("POST", "/workflows/update", {"statuses": defs, "workflows": [
            {k: wf[k] for k in ("id", "version", "name", "description", "startPointLayout", "statuses", "transitions")}]})
        print("Added to workflow:", ", ".join(n for n, _ in missing))
    else:
        print("Workflow already has Blocked and In Review.")

    # Board columns: Jira has no public API for this; use the one its own board settings page calls.
    try:
        board = call("GET", f"/board?projectKeyOrId={key}", base="/rest/agile/1.0")["values"][0]["id"]
        model = call("GET", f"/rapidviewconfig/editmodel.json?rapidViewId={board}", base="/rest/greenhopper/1.0")["rapidListConfig"]
        cols = [{"id": c["id"], "name": c["name"], "min": c["min"], "max": c["max"], "isKanPlanColumn": c["isKanPlanColumn"],
                 "mappedStatuses": [{"id": st["id"]} for st in c["mappedStatuses"]]} for c in model["mappedColumns"]]
        unmapped = {st["name"]: st["id"] for st in model["unmappedStatuses"]}
        at = next((i for i, c in enumerate(cols) if c["name"] == "Done"), len(cols))
        added = []
        for name, _ in NEW_STAGES:
            if name in unmapped and name not in {c["name"] for c in cols}:
                cols.insert(at, {"name": name, "min": "", "max": "", "isKanPlanColumn": False, "mappedStatuses": [{"id": unmapped[name]}]})
                at += 1
                added.append(name)
        if added:
            call("PUT", "/rapidviewconfig/columns", {"rapidViewId": board, "currentStatisticsField": {"id": "issueCount_"},
                                                     "mappedColumns": cols}, base="/rest/greenhopper/1.0")
        print("Board columns:", ", ".join(c["name"] for c in cols if not c["isKanPlanColumn"]))
    except (RuntimeError, KeyError, IndexError) as e:
        print(f"Could not update board columns ({e}). " + MANUAL)


def main():
    load_env()
    cmd, args = (sys.argv[1:2] or ["sync"])[0], sys.argv[2:]
    configured = all(os.environ.get(k) for k in ("JIRA_SITE", "JIRA_EMAIL", "JIRA_API_TOKEN", "JIRA_PROJECT_KEY"))
    if not configured and not os.environ.get("JIRA_DRY_RUN"):
        if cmd == "hook":
            return  # Jira not set up yet: stay silent so the office still works
        sys.exit("Jira not configured: set JIRA_SITE, JIRA_EMAIL, JIRA_API_TOKEN, JIRA_PROJECT_KEY in .env")
    s = load_state()
    try:
        {"check": check, "setup": setup, "pull": lambda: pull(s)}.get(cmd, lambda: sync(args, s))()
    except Exception as e:
        if cmd != "hook":
            raise
        with open(LOG, "a", encoding="utf-8") as fh:  # hooks must never block the agents
            fh.write(f"{datetime.now().isoformat()} {type(e).__name__}: {e}\n")


if __name__ == "__main__":
    main()
