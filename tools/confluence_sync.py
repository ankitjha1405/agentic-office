#!/usr/bin/env python3
"""Mirror workspace/confluence/ (plus CLAUDE.md and ROSTER.md) to a Confluence Cloud space.

Every folder becomes a Confluence folder, every .md file a page. Each page opens with an
info panel naming its owner (the agent who created it), department, status and dates,
taken from the doc's frontmatter (see company/documentation-standard.md).

Commands:
  sync [FILE]  push new/changed docs (all changed ones if no FILE)
  hook         same as sync, but never fails; called by Claude Code hooks

Config (env or .env): JIRA_SITE, JIRA_EMAIL, JIRA_API_TOKEN (same Atlassian login),
CONFLUENCE_SPACE_KEY (sync is off until this is set), optional CONFLUENCE_SPACE_NAME.
CONFLUENCE_DRY_RUN=1 prints API calls instead of sending them.
"""
import base64, glob, hashlib, html, json, os, re, sys, urllib.error, urllib.request
from datetime import datetime

from common import ROOT, SSL, load_env, roster, who

DOCS = os.path.join(ROOT, "workspace", "confluence")
STATE = os.environ.get("CONFLUENCE_STATE") or os.path.join(DOCS, ".confluence-state.json")
LOG = os.path.join(DOCS, ".confluence-sync.log")
# Root files that also belong in Confluence: path -> (folder, frontmatter defaults)
EXTRA = {"CLAUDE.md": ("company", {"title": "Company OS", "owner": "coo", "department": "Leadership", "status": "Approved"}),
         "ROSTER.md": ("company", {"title": "Company Roster", "owner": "coo", "department": "Leadership", "status": "Approved"})}
FOLDER_TITLES = {"prds": "PRDs", "playbooks": "Department Playbooks"}


def call(method, path, body=None):
    if os.environ.get("CONFLUENCE_DRY_RUN"):
        print(method, path, (json.dumps(body)[:110] if body else ""))
        return {"id": "dry-" + hashlib.md5((path + json.dumps(body or {})).encode()).hexdigest()[:6],
                "results": [], "version": {"number": 1}}
    auth = base64.b64encode(f"{os.environ['JIRA_EMAIL']}:{os.environ['JIRA_API_TOKEN']}".encode()).decode()
    req = urllib.request.Request(os.environ["JIRA_SITE"].rstrip("/") + "/wiki" + path, method=method,
                                 data=json.dumps(body).encode() if body is not None else None,
                                 headers={"Authorization": "Basic " + auth, "Accept": "application/json",
                                          "Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=30, context=SSL) as r:
            raw = r.read()
            return json.loads(raw) if raw else {}
    except urllib.error.HTTPError as e:
        raise RuntimeError(f"{method} {path} -> {e.code}: {e.read()[:300].decode(errors='replace')}")


# ---------- Markdown -> Confluence storage format ----------

CURRENT = {"dir": DOCS}  # folder of the doc being converted, for resolving relative links


def link(label, target):
    """Relative link to another doc -> Confluence page link; to a task file -> its Jira issue."""
    if re.match(r"[a-z]+:", target):
        return f'<a href="{html.escape(target)}">{label}</a>'
    path = os.path.normpath(os.path.join(CURRENT["dir"], target.split("#")[0]))
    key = re.match(r"([A-Z]+-\d+)-", os.path.basename(path))
    if key and os.path.dirname(path).endswith(os.path.join("workspace", "jira")):
        try:
            issue = json.load(open(os.path.join(ROOT, "workspace", "jira", ".jira-state.json"), encoding="utf-8"))["issues"][key.group(1)]["key"]
            return f'<a href="{os.environ.get("JIRA_SITE", "").rstrip("/")}/browse/{issue}">{label}</a>'
        except (OSError, KeyError, ValueError):
            pass
    if path.endswith(".md") and os.path.exists(path):
        meta, body = split_frontmatter(open(path, encoding="utf-8").read())
        title = meta.get("title") or (re.search(r"^# (.+)$", body, re.M) or [None, ""])[1]
        if title:
            return (f'<ac:link><ri:page ri:content-title="{html.escape(title)}"/>'
                    f"<ac:plain-text-link-body><![CDATA[{html.unescape(label)}]]></ac:plain-text-link-body></ac:link>")
    return label  # local-only path: keep the text, drop the dead link


def inline(text):
    parts = re.split(r"(`[^`]+`)", text)
    out = []
    for p in parts:
        if p.startswith("`") and p.endswith("`") and len(p) > 1:
            out.append("<code>" + html.escape(p[1:-1], quote=False) + "</code>")
            continue
        p = html.escape(p, quote=False)
        p = re.sub(r"\[([^\]]+)\]\(([^)\s]+)\)", lambda m: link(m.group(1), html.unescape(m.group(2))), p)
        p = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", p)
        p = re.sub(r"(?<![\w*])\*(?!\s)(.+?)(?<!\s)\*(?![\w*])", r"<em>\1</em>", p)
        out.append(p)
    return "".join(out)


def md_to_storage(md):
    lines, out, i = md.splitlines(), [], 0
    para, stack = [], []  # stack of (indent, tag) for open lists

    def flush_para():
        if para:
            out.append("<p>" + inline(" ".join(para)) + "</p>")
            para.clear()

    def close_lists(indent=-1):
        while stack and stack[-1][0] > indent:
            out.append(f"</li></{stack.pop()[1]}>")

    while i < len(lines):
        line = lines[i]
        fence = re.match(r"\s*```(\w*)", line)
        if fence:
            flush_para(); close_lists()
            body, i = [], i + 1
            while i < len(lines) and not lines[i].strip().startswith("```"):
                body.append(lines[i]); i += 1
            code = "\n".join(body).replace("]]>", "]]]]><![CDATA[>")
            lang = f'<ac:parameter ac:name="language">{fence.group(1)}</ac:parameter>' if fence.group(1) else ""
            out.append(f'<ac:structured-macro ac:name="code">{lang}<ac:plain-text-body><![CDATA[{code}]]></ac:plain-text-body></ac:structured-macro>')
            i += 1
            continue
        if line.lstrip().startswith("|") and i + 1 < len(lines) and re.match(r"\s*\|[\s:|-]+\|\s*$", lines[i + 1]):
            flush_para(); close_lists()
            cells = lambda l: [c.strip() for c in l.strip().strip("|").split("|")]
            rows = ["<tr>" + "".join(f"<th>{inline(c)}</th>" for c in cells(line)) + "</tr>"]
            i += 2
            while i < len(lines) and lines[i].lstrip().startswith("|"):
                rows.append("<tr>" + "".join(f"<td>{inline(c)}</td>" for c in cells(lines[i])) + "</tr>")
                i += 1
            out.append("<table><tbody>" + "".join(rows) + "</tbody></table>")
            continue
        h = re.match(r"(#{1,6})\s+(.*)", line)
        item = re.match(r"(\s*)([-*]|\d+\.)\s+(.*)", line)
        if h:
            flush_para(); close_lists()
            out.append(f"<h{len(h.group(1))}>{inline(h.group(2))}</h{len(h.group(1))}>")
        elif item:
            flush_para()
            indent, tag = len(item.group(1)), "ol" if item.group(2)[0].isdigit() else "ul"
            text = re.sub(r"^\[ \]\s*", "☐ ", re.sub(r"^\[[xX]\]\s*", "☑ ", item.group(3)))
            close_lists(indent)
            if stack and stack[-1][0] == indent:
                out.append("</li><li>" + inline(text))
            else:
                out.append(f"<{tag}><li>" + inline(text))
                stack.append((indent, tag))
        elif re.match(r"\s*(---|\*\*\*)\s*$", line):
            flush_para(); close_lists(); out.append("<hr/>")
        elif line.startswith(">"):
            flush_para(); close_lists(); out.append("<blockquote><p>" + inline(line.lstrip("> ")) + "</p></blockquote>")
        elif not line.strip():
            flush_para(); close_lists()
        elif stack and line.startswith(" "):
            out.append(" " + inline(line.strip()))  # continuation of a list item
        else:
            close_lists(); para.append(line.strip())
        i += 1
    flush_para(); close_lists()
    return "".join(out)


# ---------- docs ----------

def split_frontmatter(text):
    if text.startswith("---\n"):
        _, fm, body = text.split("---", 2)
        meta = {}
        for line in fm.strip().splitlines():
            k, _, v = line.partition(":")
            meta[k.strip()] = v.strip()
        return meta, body.lstrip("\n")
    return {}, text


def owner_panel(meta, rel, names):
    def person(a):
        return html.escape(who(a, names) if a else "Unassigned — add an owner")
    contributors = ", ".join(person(c.strip()) for c in meta.get("contributors", "").strip("[]").split(",") if c.strip())
    rows = [("Owner", person(meta.get("owner"))), ("Department", meta.get("department", "")),
            ("Status", meta.get("status", "Draft")), ("Created", meta.get("created", "")),
            ("Last updated", meta.get("updated", "")), ("Contributors", contributors), ("Source", f"<code>{html.escape(rel)}</code>")]
    cells = " · ".join(f"<strong>{k}:</strong> {v if k in ('Owner', 'Contributors', 'Source') else html.escape(v)}"
                       for k, v in rows if v)
    return f'<ac:structured-macro ac:name="info"><ac:rich-text-body><p>{cells}</p></ac:rich-text-body></ac:structured-macro>'


def docs():
    """(abs path, relative folder parts, meta defaults)"""
    found = []
    for f in sorted(glob.glob(os.path.join(DOCS, "**", "*.md"), recursive=True)):
        rel = os.path.relpath(f, DOCS)
        if not any(p.startswith(".") for p in rel.split(os.sep)):
            found.append((f, rel.split(os.sep)[:-1], {}))
    for name, (folder, defaults) in EXTRA.items():
        found.append((os.path.join(ROOT, name), [folder], defaults))
    return found


def load_state():
    try:
        return json.load(open(STATE, encoding="utf-8"))
    except (OSError, ValueError):
        return {"space": None, "folders": {}, "pages": {}}


def save_state(s):
    json.dump(s, open(STATE, "w", encoding="utf-8"), indent=1)


def write_home(page_id, name):
    """Turn a new space's blank home page into an index of the space."""
    jira = os.environ.get("JIRA_PROJECT_KEY")
    jira_link = (f' Work tracking lives in <a href="{html.escape(os.environ["JIRA_SITE"].rstrip("/"))}/browse/'
                 f'{html.escape(jira)}">Jira ({html.escape(jira)})</a>.') if jira else ""
    body = ('<ac:structured-macro ac:name="info"><ac:rich-text-body><p><strong>Owner:</strong> Ankit Jha (coo) · '
            '<strong>Maintained by:</strong> Bhavna Trivedi (knowledge-steward)</p></ac:rich-text-body></ac:structured-macro>'
            '<p>Company documentation for the agentic office. Every page is written by the agent named in its owner panel '
            f'and kept in sync automatically from the office workspace.{jira_link}</p>'
            '<h2>How this space is organized</h2><ul><li><strong>Company</strong>: Company OS, roster, architecture, '
            'documentation standard</li><li><strong>Department Playbooks</strong>: how each department works</li>'
            '<li><strong>Products</strong>: one folder per product with overview, scope, functional spec, technical design, '
            'test cases and release notes</li><li><strong>Templates</strong>: templates for agent profiles and documents</li></ul>'
            '<p>Rules for writing here: <ac:link><ri:page ri:content-title="Documentation Standard"/></ac:link>.</p>'
            '<h2>All pages</h2><ac:structured-macro ac:name="pagetree"><ac:parameter ac:name="root"><ac:link>'
            '<ri:page ri:content-title="@self"/></ac:link></ac:parameter><ac:parameter ac:name="expandCollapseAll">true'
            '</ac:parameter></ac:structured-macro>')
    version = call("GET", f"/api/v2/pages/{page_id}")["version"]["number"]
    call("PUT", f"/api/v2/pages/{page_id}", {"id": page_id, "status": "current", "title": name,
                                             "body": {"representation": "storage", "value": body},
                                             "version": {"number": version + 1, "message": "Space index"}})


def ensure_space(s):
    if s["space"]:
        return s["space"]
    key = os.environ["CONFLUENCE_SPACE_KEY"]
    found = call("GET", f"/api/v2/spaces?keys={key}")["results"]
    if found:
        space = {"id": found[0]["id"], "home": found[0].get("homepageId")}
    else:
        name = os.environ.get("CONFLUENCE_SPACE_NAME", "Agentic Office")
        call("POST", "/rest/api/space", {"key": key, "name": name, "description": {"plain": {
            "value": "Company documentation for the agentic office. Mirrored from workspace/confluence.", "representation": "plain"}}})
        got = call("GET", f"/api/v2/spaces?keys={key}")["results"] or [{"id": "dry-space", "homepageId": "dry-home"}]
        space = {"id": got[0]["id"], "home": got[0].get("homepageId")}
        write_home(space["home"], name)
    s["space"] = space
    save_state(s)
    return space


def ensure_folder(parts, s):
    """Folder for a path like ['products', 'tic-tac-toe']; parents first. Returns its id."""
    space = ensure_space(s)
    parent = space["home"]
    for n in range(1, len(parts) + 1):
        key = "/".join(parts[:n])
        if key not in s["folders"]:
            name = parts[n - 1]
            title = FOLDER_TITLES.get(name, name.replace("-", " ").title())
            body = {"spaceId": space["id"], "title": title, "parentId": parent}
            try:
                s["folders"][key] = call("POST", "/api/v2/folders", body)["id"]
            except RuntimeError as e:
                if "already exists" not in str(e) and "title" not in str(e).lower():
                    raise
                body["title"] = f"{title} ({key})"  # titles are unique per space
                s["folders"][key] = call("POST", "/api/v2/folders", body)["id"]
            save_state(s)
        parent = s["folders"][key]
    return parent


def sync_doc(path, folder, defaults, s, names):
    text = open(path, encoding="utf-8").read()
    digest = hashlib.md5(text.encode()).hexdigest()
    rel = os.path.relpath(path, ROOT)
    page = s["pages"].get(rel)
    if page and page.get("hash") == digest:
        return
    meta, body = split_frontmatter(text)
    meta = defaults | meta
    title = meta.get("title") or (re.search(r"^# (.+)$", body, re.M) or [None, os.path.basename(path)[:-3]])[1]
    if meta.get("title"):
        body = re.sub(r"^# .+\n", "", body, count=1)  # the page title already shows it
    CURRENT["dir"] = os.path.dirname(path)
    storage = owner_panel(meta, rel, names) + md_to_storage(body)
    parent = ensure_folder(folder, s) if folder else ensure_space(s)["home"]
    space = s["space"]["id"]
    if not page:
        req = {"spaceId": space, "status": "current", "title": title, "parentId": parent,
               "body": {"representation": "storage", "value": storage}}
        try:
            created = call("POST", "/api/v2/pages", req)
        except RuntimeError as e:
            if "title" not in str(e).lower():
                raise
            req["title"] = f"{title} ({rel})"
            created = call("POST", "/api/v2/pages", req)
        page = s["pages"][rel] = {"id": created["id"], "version": 1, "title": req["title"]}
        save_state(s)  # before the label call, so a failure there cannot make the rerun create a second page
    else:
        page["version"] += 1
        call("PUT", f"/api/v2/pages/{page['id']}", {"id": page["id"], "status": "current", "title": page["title"],
                                                     "body": {"representation": "storage", "value": storage},
                                                     "version": {"number": page["version"], "message": f"Synced from {rel}"}})
    if not page.get("labeled", "hash" in page):  # pages synced before this flag existed already have labels
        owner = meta.get("owner")
        labels = [{"prefix": "global", "name": n} for n in
                  ["office", f"owner-{owner}" if owner else "owner-missing",
                   re.sub(r"[^a-z0-9-]", "", meta.get("department", "").lower().replace(" ", "-").replace("&", "and"))] if n]
        call("POST", f"/rest/api/content/{page['id']}/label", labels)
        page["labeled"] = True
    page["hash"] = digest
    save_state(s)


def sync(files, s):
    names = roster()
    wanted = {os.path.abspath(f) for f in files}
    for path, folder, defaults in docs():
        if not wanted or path in wanted:
            sync_doc(path, folder, defaults, s, names)


def main():
    load_env()
    cmd, args = (sys.argv[1:2] or ["sync"])[0], sys.argv[2:]
    configured = all(os.environ.get(k) for k in ("JIRA_SITE", "JIRA_EMAIL", "JIRA_API_TOKEN", "CONFLUENCE_SPACE_KEY"))
    if not configured and not os.environ.get("CONFLUENCE_DRY_RUN"):
        if cmd == "hook":
            return  # Confluence not switched on yet: stay silent so the office still works
        sys.exit("Confluence not configured: set CONFLUENCE_SPACE_KEY (and the JIRA_* login) in .env")
    s = load_state()
    try:
        sync(args, s)
    except Exception as e:
        if cmd != "hook":
            raise
        with open(LOG, "a", encoding="utf-8") as fh:  # hooks must never block the agents
            fh.write(f"{datetime.now().isoformat()} {type(e).__name__}: {e}\n")


if __name__ == "__main__":
    main()
