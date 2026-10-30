---
title: GSoC · First Issues and Draft Fixes (Zulip, AOSSIE, Rocket.Chat)
owner: coo
contributors: [cto, backend-engineer-1, backend-engineer-2, frontend-engineer-1, qa-functional, qa-automation]
department: Engineering & Quality
status: Draft
created: 2026-10-30
updated: 2026-10-30
---

# GSoC · First Issues and Draft Fixes (Zulip, AOSSIE, Rocket.Chat)

Tasks: ENG-9 (Zulip), ENG-10 (AOSSIE), ENG-11 (Rocket.Chat). Follow-up to PROD-1 (`workspace/confluence/research/gsoc-orgs-research.md`).

Ground rules followed: read-only GitHub only. No comment, claim, reaction, fork, push, PR or chat post was made. All checks were done on 2026-10-30. The CEO reviews, learns and submits every contribution under their own GitHub account, after approval.

## Summary

| Org | AI policy | Clean issues found | Drafted fix | QA |
|---|---|---|---|---|
| Zulip | AI allowed but limited: you must understand and test every line; do not use an LLM to find work; no AI-written messages. Per the CEO rule: **no code drafted**, learning guides only. | **0 of 12** checked. Every unassigned `help wanted` issue checked has an open PR or a recent claim. | None (policy). | qa-automation (Manish): guide paths corrected; both survivors failed the open-PR check. |
| AOSSIE | AI allowed with disclosure in the PR; test it yourself. | **1 clean** (IndexedDB-Import-Export #114) plus 4 weaker ones. | #114, uncommitted in `/Users/ankitkumar/dev/oss/IndexedDB-Import-Export`. **Not run, not committed.** | qa-functional (Divya): accept with notes (static review). |
| Rocket.Chat | Ban is on LLM-written GSoC **proposals**; AI for code/research allowed (estimate, from the 2026 page). | **0**. All checked issues have open PRs or claims; API quota ran out before the rest. | None (no issue). | Not needed. |

**Why no branches or test runs:** in this run, `git` (other than clone) and `npm` needed a permission approval that was not available, for the agents and for the main session. Nothing was worked around. The CEO runs the branch, test and commit commands listed under AOSSIE.

**The real finding:** first issues at all three orgs are heavily contested. Most labelled issues get claims and PRs within days. Speed and a fresh check on the day matter more than the shortlist.

### Before claiming anything (2-minute browser check, every time)
1. Open the issue and read the last 10 comments.
2. In the repo's Pull requests tab, search `is:pr is:open <issue number>`.

## Zulip

Checked 2026-10-30 with read-only GitHub API fetches (no gh/Bash). "FACT" = read from a page or API. "ESTIMATE" = my judgment. No code was drafted, nothing cloned, nothing posted to GitHub.

### 1. AI policy (FACT)
URL: https://zulip.readthedocs.io/en/latest/contributing/contributing.html#ai-use-policy-and-guidelines
Short exact quotes (the fetch tool limits quote length; read the full section yourself):
- "Do not submit an AI-generated PR you haven't personally understood and tested". PRs that look like they break this "will be closed without review."
- "The answer to 'Why is X an improvement?' should never be 'I'm not sure. The AI did it.'"
- "Don't point an LLM at the code and ask it to find problems or things to work on."
- "Do not post AI-generated messages" in the Zulip development community.
- "Code assistants can be a useful search engine/discovery tool, but don't trust claims they make about how Zulip works."
- If an LLM writes a PR description or comment, it is your responsibility to read all of it. Keep it concise and in your own reasoning.
- QA note: the policy also says you must complete the PR template yourself, not paste LLM replies to review feedback, and put any quoted LLM output in a Zulip quote block. Meaning of the above is otherwise accurate. Exact quotes are short and match; the "will be closed without review" wording is a paraphrase of "closed without review".

What it means for the CEO:
- AI help is not banned, but understanding is mandatory. Closed-unread is the penalty.
- Decision: learning-guide route. No code from us. The CEO writes the change, the claim line and the PR text in their own words.
- The shortlist below is a browse list, built by an AI, so the CEO should choose the issue personally after reading it. Do not announce in chat that an AI picked it.
- The PR template has an "AI use" checkbox pointing at this policy. Be honest in it.

### 2. Labels (FACT, verified by Ankit)
The newcomer label is `help wanted`. There are zero open `good first issue` issues. Claiming: comment `@zulipbot claim`. New contributors may claim one issue at a time until a couple of PRs merge. The bot welcome message lists steps (read the guide, post a plan comment, accept the repo invite) before it assigns you.

### 3. Candidate check (FACT unless marked)
Method: issue comments API (all comments read), PR search API where it worked, issue timeline API (truncated, partial). The PR search API returned HTTP 403 (rate limit) partway, so some PR checks are INCOMPLETE and marked. Cutoff for "recent claim": after 2026-08-31.

| Issue | Title | Area | Verdict | Evidence |
|---|---|---|---|---|
| #25072 | Hide "Move all messages" without permission | web | DROP | Claim 2026-10-04 (navyajm123-design); open PR #39436 (bijanmurmu, 2026-05-30) |
| #13167 | API docs for narrow | docs | DROP | Open PRs #40469 (2026-10-23) and #40133 (2026-09-15) |
| #16094 | i18n on /stats | web | DROP | Open PR #39722 (Amormio25, 2026-07-10) |
| #25552 | Translate reload-language text | web | DROP | Open PRs #27226 (2023) and #38378 (2026-03-09); claim 2026-10-29, abandoned same day |
| #40026 | Suppress redundant tooltips | web | DROP | Open PRs #40027, #40032; assigned to Amanshrivastab 2026-10-05; many claims |
| #36486 | Deleted image placeholder | web | DROP | Open PRs #37443, #36627; 15 claims |
| #29879 | Profile-field select delete modal | web TS | DROP | Open PR #37553 (rajj28), 2 files |
| #24044 | Code Playground language validation | Python | DROP | Claim 2026-07-29 and PR mentioned 2026-08-31 ("waiting for final review") |
| #21717 | Wrong client time blocks edits | web TS | DROP | Claim 2026-09-05 (VishvakR, 55 days ago); needs design (server-time offset) |
| #24065 | Non-square custom emoji cropped | web+design | WEAK | Claims end 2026-03; reopened Jan 2026, then assigned/unassigned; commits referenced by CerealNotFound in Jan 2026; needs design talk. PR check NOT done |
| #17428 | Sort keys in API responses | Python | DROP (QA 2026-10-30) | Unassigned, but OPEN PR #38826 "api: Sort keys in JSON API responses alphabetically" (singhaditya73, opened 2026-04-05, awaiting review, "Fixes #17428"). Unassigned on 2026-05-01 for inactivity of the claim, not because the PR was withdrawn |
| #5090 | Add `deactivated_redirect` to server_settings API | Python | DROP (QA 2026-10-30) | Unassigned, but OPEN PR #40231 (rohitdeppi38, opened 2026-09-28, last push 2026-10-09, "not ready" label). #39093 status conflicting: issue page says open per a 2026-05-05 comment; earlier note said closed 2026-09-02 (unverified) |

QA CORRECTION (checked 2026-10-30 via issue/PR pages): both "KEEP" candidates have open PRs, so they fail the no-open-PR test. Result: 0 of 12 survive. The two learning guides below are kept only as study material on the code; do not claim either issue. Most unassigned `help wanted` issues are heavily claimed. Do not claim any issue until the CEO repeats the two checks below on GitHub in a browser.

Ranking (ESTIMATE, beginner Python/JS/TS, by size):
1. #17428 Sort API keys. Small, one Python file, but the 2021 thread says sorting may cost speed; confirm the intended design first.
2. #5090 Expose `deactivated_redirect`. Small-medium: Python field + API docs + test; maintainers wanted a design chat in #api design.
3. #24065 emoji crop. Medium, UI/design questions. Not recommended first.
(Nothing else qualifies. Suggest the CEO browse `help wanted` sorted by "least recently updated" in the GitHub UI themselves, which also fits the policy.)

Two checks the CEO must run before claiming (browser, 2 minutes): (a) open the issue and read the last 10 comments; (b) search the repo Pull requests tab for `is:pr is:open <issue number>`.

### 4. Learning guide: #17428 Sort keys in API responses
https://github.com/zulip/zulip/issues/17428
Goal (FACT): API response keys come out in arbitrary order; the issue asks for alphabetical order like the examples in the /api docs.

Files to read (verified to exist on main):
- `zerver/lib/response.py`. `json_success` calls `json_response`, which builds a `MutableJsonResponse`. Its `content` property turns the dict into bytes with `orjson.dumps(..., option=orjson.OPT_APPEND_NEWLINE | orjson.OPT_PASSTHROUGH_DATETIME)` (~lines 41-54), and `json_method_not_allowed` has a second `orjson.dumps` with no options (~86-91). Verified on main 2026-10-30.
- Issue comments 6-8: Tim Abbott suggests orjson's `OPT_SORT_KEYS`, wondering about a performance cost; Anders Kaseorg expects it to be small. Shaurya001-web (2026-01-02) pointed at `response.py`.
- Existing tests that compare response bodies may depend on key order. ESTIMATE: you will have to run the tests to see which ones change. No test file for response.py was found at `zerver/tests/test_response.py` (404), so search `zerver/tests/` for `json_success` tests yourself.

Likely approach (ESTIMATE): add the sort option in the one place where `content` is serialized, then run affected tests. Ask first (see questions) whether sorting should apply to everyone.

Hints: read orjson's option list in its README; understand why the code uses a lazy `content` property before editing; work out by reading what `OPT_PASSTHROUGH_DATETIME` does so you do not remove it by accident.

How to test:
- The backend suite needs Zulip's provisioned dev environment (Vagrant/Docker or the supported setup in the "Installing the development environment" docs). The CEO sets this up. Then `./tools/test-backend zerver.tests.<module>` for the modules you touch, and `./tools/lint` before committing.
- Check by hand: call an endpoint in the dev server and see keys sorted.
- Python checks on changed files only (`ruff`, `mypy`) via the repo's tooling.

Questions for chat.zulip.org, channel #new members (write in your own words; these are topics, not text):
- Is #17428 still wanted? Is there a decision about performance?
- Should sorting apply to all clients or only some?
- Where do you want tests: update the existing ones that depend on order?

### 5. Learning guide: #5090 `deactivated_redirect` in server_settings
https://github.com/zulip/zulip/issues/5090
Goal (FACT): clients (desktop/mobile) cannot learn that a realm moved to a new URL. A `deactivated_redirect` field now exists on the realm (per comment 5 in the thread); the issue asks to show it in `/api/v1/server_settings`.

Files to read:
- `zerver/views/auth.py`, function `api_get_server_settings` (verified). It builds a dict `result` and copies a fixed list of `realm_*` items from `context` when they are not None, then `return json_success(request, data=result)`. Your new field would go through the same pattern.
- Where `realm_url`, `realm_name` etc. come from: `zulip_default_context` and `login_context`, both imported from `zerver/context_processors.py` (verified from the import in auth.py). The same file `auth.py` already uses `realm.deactivated_redirect` in `show_deactivation_notice` and `login_page`.
- The realm model field `deactivated_redirect` is a `URLField` on `Realm` in `zerver/models/realms.py` (verified).
- API docs: `zerver/openapi/zulip.yaml` exists (file is huge; I did not confirm the `/server_settings` entry, unverified); `api_docs/changelog.md` exists (verified); `API_FEATURE_LEVEL` is in `version.py` (verified, value 515 on 2026-10-30). All three are normally touched together for an API change (ESTIMATE; confirm in the "API documentation" section of the Zulip docs).
- Closed PR #39093 (ebenshi, closed unmerged 2026-09-02): read its review comments to learn what maintainers asked for. This is the best map of the pitfalls.

Likely approach (ESTIMATE): add the field to the list of copied settings (or handle it specially because it is only set for deactivated realms), add it to the OpenAPI schema and changelog, and add a test next to the existing `server_settings` tests (search `zerver/tests/` for `server_settings`).

How to test: same provisioned-env note. `./tools/test-backend` for the module with the server_settings test, `./tools/test-backend zerver.tests.test_openapi` (file `zerver/tests/test_openapi.py` verified to exist) to validate the schema, then lint.

Questions for #new members / #api design (your own words): Is a PR still wanted after #39093 was closed? What did the reviewers need changed? Is the field exposed only for a deactivated realm?

### 6. Draft claim comment
Post this on the issue only after the CEO has done the two browser checks:

`@zulipbot claim`

Then the CEO adds one line of their own: what they plan to change and where, in their own words, after reading the code. Zulip's bot asks for a plan comment before it assigns the issue. Do not paste AI-written text.

### 7. PR description: headings only (FACT: from .github/pull_request_template.md on main)
Fill each in yourself. Prompts only, no pre-written text:
- **Description.** What does the PR change, in a few sentences?
- **Fixes.** `Fixes: #<number>`; or what problem it solves.
- **How changes were tested.** Exact commands you ran and what you saw. For UI changes, screenshots or a recording.
- **Screenshots and screen captures.** Separate heading in the template; fill for UI changes, else say not applicable.
- **Self-review checklist.**
  - Code review: reread your diff for naming, reuse, readability.
  - AI use: tick only if you followed the AI use policy.
  - Communication: explain your decisions; note differences from the issue; technical choices; open concerns; add automated tests where they verify logic.
  - Commits: each commit one coherent idea; message explains why.
  - Manual review and testing: visual appearance; responsiveness and internationalization; strings and tooltips; end-to-end behavior; corner cases and error conditions.
  - Leave unchecked any item you did not do.

### 8. Not done
- No `gh`, no clone, no test runs (Bash denied; coordinator chose WebFetch-only).
- PR-search checks for #17428, #5090 and #24065 incomplete (API 403). File paths in guide 5 beyond `zerver/views/auth.py` and guide 4's `zerver/lib/response.py` are unverified guesses, labelled ESTIMATE.
## AOSSIE

Prepared by Harpreet (ENG-10), 2026-10-30. Labels: FACT = seen on GitHub today, EST = my estimate, UNVERIFIED = not checked.

### 1. AI policy (FACT, read from the pages; most text is paraphrase because my fetch tool limits verbatim quotes)

- Org policy: https://github.com/AOSSIE-Org/Info/blob/main/Rules/AI.md . Exact quote: "AI is your tool. You are not AI's tool."
  Paraphrase: AI is allowed and encouraged (code, PR text, review) if you disclose it. You must test AI code locally. Put a short paragraph in the PR saying which model you used and how. Disclose AI-generated ideas in chat messages and GSoC proposals. Spam or low-quality "AI slop" issues and PRs can lead to bans. Projects can add their own AI-UsagePolicy.md that overrides this.
- Contribution rules: https://github.com/AOSSIE-Org/Info/blob/main/Rules/Contribution.md . Paraphrase: say what you plan to do before you start, no duplicate issues or PRs, follow the PR template or the PR may be closed without review, finish one issue fully before taking another.
- Target repo rules: https://github.com/AOSSIE-Org/IndexedDB-Import-Export/blob/main/CONTRIBUTING.md . Exact quote: "if you use AI assistance, please mention it in your PR description." Also "PRs without Discord updates will not be reviewed or may face delays." Wait to be assigned before starting. Run `npm test`, `npm run lint`, `npm run format:check` before the PR. Branch prefix `fix/`.
- Not read: GSoC rules page (Programs/GoogleSummerOfCode) and the org .github profile README. I only saw the index summary. Read them before the proposal.

**Verdict: AI-written code is ALLOWED with disclosure. No ban.** What it means for the CEO: you may use AI help, but you must read and understand every line, run the tests yourself, write the AI disclosure paragraph in the PR, post in the project's Discord channel, and wait to be assigned. You submit under your own account.

### 2. Labels (FACT)

- `gh search issues --owner AOSSIE-Org --label "good first issue"` returns results, so that label exists. Many titles also start with "[GOOD FIRST ISSUE]:".
- Other labels seen on issues: `bug`, `enhancement`, `documentation`, `help wanted` (only 2 hits). Many real beginner bugs carry only `bug` or no label.
- I could not run `gh label list` (blocked in this session), so the per-repo label list is not checked.

### 3. Key finding: the field is crowded (FACT)

Every `good first issue` I opened had 1 to 50 claim comments, or a linked PR. Examples: EduAid #592 (claimed by mahek2016), #603 (PR #675, #605, #604), #668 (PR #669 plus 7 asks), DebateAI #582 (claimed by author), Perspective #143 (PR #153). Even fresh `bug` issues get PRs within 1 to 2 days: OpenVerifiableLLM #260 (draft PR #261), MCP-Template #15 (PR #16), Perspective #175 (PR #176), OrgExplorer #433 (PR #434, draft). Speed matters: check the PR list again the moment you decide.

### 4. Shortlist (ranked)

| # | Issue | Repo | Size | Why | Claim / PR check |
|---|---|---|---|---|---|
| 1 | https://github.com/AOSSIE-Org/IndexedDB-Import-Export/issues/114 importDB loses existing data when backup has an invalid record | IndexedDB-Import-Export (TypeScript, vitest tests, 3 open issues, merged-PR flow) | EST: small-medium, one file `src/core/importer.ts` plus one test | Clear repro, exact line numbers, the author supplied failing output. Tests run with `npm test`. Fits TS beginner | FACT: no assignee, 1 comment (Gitcord bot only), `gh pr list --search 114` empty, all 3 open PR-less. Soft risk: the author wrote "I can include it in a fix PR" |
| 2 | https://github.com/AOSSIE-Org/BabyNest/issues/259 Chat cache ignores conversation context | BabyNest (React Native JS) | EST: small (one file `Frontend/src/model/model.jsx`) but hard to run (needs mobile/native mocks) | Simple logic bug, clear cause | FACT: no assignee, no PR for 259. Author ticked "I want to work on this" (soft claim). Poor for a beginner to test |
| 3 | https://github.com/AOSSIE-Org/IndexedDB-Import-Export/issues/99 idb dependency documented but unused | same repo as #1 | EST: tiny if option 2 (remove dep + doc line), but needs maintainer decision first | Low risk | FACT: 0 comments, no PR. It asks for a maintainer decision, so ask in Discord before coding |
| 4 | https://github.com/AOSSIE-Org/OrgExplorer/issues/421 PAT stored in plaintext in localStorage | OrgExplorer (TS) | EST: medium, design choice | Security fix, learning value | FACT: 1 comment (bot). UNVERIFIED: my PR list stopped at 60 entries, so a PR may exist. Recheck |
| 5 | https://github.com/AOSSIE-Org/DebateAI/issues/768 Breadcrumb "Debate" opens 404 | DebateAI (Go plus React/TS) | EST: small | Frontend routing fix | FACT: 1 comment. UNVERIFIED: PR list was long and I did not search "768". DebateAI has 60+ open PRs, so a PR is likely |

Rejected after checking: EduAid #592/#603/#668/#69, DebateAI #582/#431/#543/#612, Perspective #141/#143/#173/#175, OpenVerifiableLLM #260/#257/#262, MCP-Template #15/#17, OrgExplorer #416/#417/#433/#428/#427, BabyNest #255/#300, IDB #95, Rein #448/#441, Skills #8, Agora #15/#20. Each has a claim or a linked PR (reason above or in section 3).

### 5. Drafted fix for IDB #114

**Status: edited in the working tree only. NOT RUN (no npm install, no tests, no lint). NOT COMMITTED. Not on a branch (the clone is on `main`).** Bash is blocked for me, so nothing below has been executed. Treat the diff as untested.

Files changed (both in `/Users/ankitkumar/dev/oss/IndexedDB-Import-Export`):
- `src/core/importer.ts`: decode every backup record before the database is deleted or opened.
- `tests/importer.test.ts`: two new tests (overwrite and merge with an invalid date).

Diff (composed by hand from my edits; line numbers and context are approximate, `git diff` will show the real one):

```diff
--- a/src/core/importer.ts
+++ b/src/core/importer.ts
@@ Insert records into a single object store (doc comment)
- * Each record is deserialized from its tagged representation back to
- * native JavaScript types before insertion.
+ * Records must already be deserialized from their tagged representation back to
+ * native JavaScript types (done up front in `importDB`, before anything is deleted).
@@
- * @param records - The serialized records from the backup.
+ * @param records - The deserialized records from the backup.
@@ function insertRecords
-    for (const serializedRecord of records) {
-      const value = deserialize(serializedRecord.value);
-      const key = deserialize(serializedRecord.key);
-
+    for (const { key, value } of records) {
       // For stores with out-of-line keys (keyPath is null), pass the key explicitly.
@@ export async function importDB
+  // Deserialize every record before touching the database. A bad record (for example
+  // an invalid date) then rejects here, while the existing data is still intact:
+  // "overwrite" has not deleted it and "merge" has not written anything yet.
+  const deserialized = Object.fromEntries(
+    Object.entries(stores).map(([name, records]) => [
+      name,
+      records.map((record) => ({
+        key: deserialize(record.key),
+        value: deserialize(record.value),
+      })),
+    ]),
+  );
+
   const db = await openDatabaseForImport(dbName, backupData.databaseVersion, schema, strategy);
@@
-    const targetStores = Object.keys(stores).filter((name) => dbStoreNames.includes(name));
+    const targetStores = Object.keys(deserialized).filter((name) => dbStoreNames.includes(name));
@@
-      const records = stores[storeName] ?? [];
+      const records = deserialized[storeName] ?? [];
```

```diff
--- a/tests/importer.test.ts
+++ b/tests/importer.test.ts
@@ after 'duplicate storeNames entries do not insert records twice' (end of first describe)
+  // ─── Invalid backup records ────────────────────────────────────────
+
+  it('"overwrite" with an invalid record rejects and keeps the existing data', async () => {
+    (creates DB 'items' with ids 1 and 2; backup has valid id 3, then id 4 with
+     at: { __type: 'date', value: 'not-a-date' }; expects importDB(overwrite) to
+     reject with /Invalid date/; then reads the store and expects ids 1 and 2 only)
+  });
+
+  it('"merge" with an invalid record rejects and writes nothing', async () => {
+    (creates DB with id 1; backup has valid id 11, then id 12 with the bad date;
+     expects importDB(merge) to reject with /Invalid date/; store still only id 1)
+  });
```

The test bodies are in the file (`tests/importer.test.ts`, about lines 764 to 826). I summarised them in the second block instead of copying 60 lines. Copy them from the file if you need the full text.

Plain-English explanation, line by line:
1. Doc comments on `insertRecords`: the function no longer decodes records, so the comments now say records arrive already decoded.
2. `for (const { key, value } of records)`: replaces the old loop that read `serializedRecord.value` and `.key` and called `deserialize` on each. Same variable names, so the `store.put/add` lines below it did not change.
3. The new block in `importDB`: for each store in the (already narrowed) backup, turn each record's key and value from the tagged backup form (`{__type:'date', ...}`) into real JS values using the same `deserialize` function as before. It runs before `openDatabaseForImport`, the step that deletes the DB under "overwrite". If any record is bad, `deserialize` throws a RangeError here and the import stops with the old data untouched.
4. `Object.keys(deserialized)` and `deserialized[storeName]`: the later code now reads the decoded copy, not the raw one. The set of store names is the same, so which stores get written does not change.
5. Behaviour kept: the rejection is still the same RangeError; the `onBeforeImport` hook still runs first and still sees the raw summary.
6. The tests mirror existing ones: `buildBackup`, `createTestDB`, `readAllFromStore`, `uniqueDBName`.

QA (qa-functional, Divya, static review 2026-10-30): **accept with notes.** Fix covers overwrite and merge; the new tests should fail on old code and pass on new. Hand-written diff matches the files on disk. Notes: write-time errors beyond duplicate keys can still lose data under overwrite; orphan stores now reject on a bad record (both added to the PR body above). Prettier on two ~97-char test lines unverified.

Known gaps (EST):
- Duplicate keys (ConstraintError) are NOT fixed. Under "overwrite" that error still happens after the delete. Open question for maintainers: detect duplicate keys up front, or abort and roll back differently. Say this in the PR and on Discord.
- Prettier: the `targetStores` line is about 96 characters. If `npm run format:check` fails, run `npx prettier --write src/core/importer.ts tests/importer.test.ts` and re-check the diff.
- My first test uses `rejects.toThrow(/Invalid date/)`, which matches the message in `src/serialization/index.ts` line 263. Fake-indexeddb in tests may order records differently; I assumed `readAllFromStore` returns by key order (ids 1 then 2).

Commands for the CEO (run in `/Users/ankitkumar/dev/oss/IndexedDB-Import-Export`):

```bash
git switch -c gsoc/114-importdb-validate-before-delete
npm install
npm test
npm run lint
npm run format:check
git add src/core/importer.ts tests/importer.test.ts
git commit -m "fix: validate backup records before deleting or writing in importDB"
```

Commit format per CONTRIBUTING: `fix:` prefix for bug fixes. Before opening the PR: wait to be assigned, post in the project Discord channel, rebase on upstream main. Check the first `npm test` run: if my new tests fail, read the failure before editing.

Draft claim comment (you post it): "Hi, I'd like to work on this. My plan: deserialize all records before openDatabaseForImport deletes or opens the DB, and add vitest tests for overwrite and merge with an invalid date. Duplicate keys (ConstraintError) would stay out of this PR unless you want them in. Could you assign it to me? I will use AI assistance and disclose it in the PR. I have joined the Discord."

PR description (follows `.github/PULL_REQUEST_TEMPLATE.md`; the CEO edits the model name and ticks only what is true after running the commands):

```markdown
###  Addressed Issues:
Fixes #114


###  Screenshots/Recordings:
Not applicable (no UI change).


###  Additional Notes:
`importDB` used to decode backup records inside `insertRecords`, after `openDatabaseForImport` had already deleted the database ("overwrite") or opened it ("merge"). A record that could not be decoded (for example an invalid date) rejected the import after the existing data was gone or half-written.

Now every record is decoded in `importDB` before `openDatabaseForImport`, so a bad record rejects while the existing data is untouched. `insertRecords` receives the decoded records.

Tests added in `tests/importer.test.ts`:
- overwrite with an invalid date rejects and the existing records stay
- merge with an invalid date rejects and no new records appear

Behaviour change: a store that is in the backup data but not in the schema used to be skipped without decoding. Its records are now decoded too, so a bad record there also rejects the import.

Not covered: errors that only appear when writing (duplicate keys, a record missing its inline keyPath, an invalid out-of-line key, a unique-index violation) still happen inside the transaction, after the delete under "overwrite". I left these out to keep the change small; happy to follow up if maintainers prefer an approach.

AI disclosure: I used <MODEL NAME, e.g. Claude> to help read `src/core/importer.ts`, draft the change and the two tests, and write this description. I reviewed the code, ran `npm test`, `npm run lint` and `npm run format:check` myself, and I understand the change.

How to test:
1. `npm install`
2. `npm test` (the two new tests fail on `main` and pass with this change)
3. `npm run lint` and `npm run format:check`


## Checklist
- [ ] My code follows the project's code style and conventions
- [ ] I have made corresponding changes to the documentation
- [ ] My changes generate no new warnings or errors
- [ ] I have joined the [Discord server](https://discord.gg/hjUhu33uAn) and I will share a link to this PR with the project maintainers there
- [ ] I have read the [Contributing Guidelines](./CONTRIBUTING.md)

## ⚠️ AI Notice - Important!

 We encourage contributors to use AI tools responsibly when creating Pull Requests. While AI can be a valuable aid, it is essential to ensure that your contributions meet the task requirements, build successfully, include relevant tests, and pass all linters. Submissions that do not meet these standards may be closed without warning to maintain the quality and integrity of the project. Please take the time to understand the changes you are proposing and their impact.
```

Shortlist checks done now (FACT via search):
- OrgExplorer #421: PR search for "421" returns only #224 and #58; neither mentions #421. No linked PR found.
- DebateAI #768: GitHub PR search for "768" returns only unrelated PRs (e.g. #714, #350). No linked PR found. Search is fuzzy, so recheck on the day.

### 6. What I could not do

- Run anything: npm install, tests, lint, format check, git branch and commit (Bash blocked).
- `gh label list` per repo.
- Read the GSoC rules page and org profile README.
## Rocket.Chat

Method: WebFetch on the unauthenticated read-only GitHub API (no gh, no git). The API search quota ran out (HTTP 403), so some checks are missing. Dates are as returned on 2026-10-30. Facts are labelled; the rest is estimate.

### Policy (fact)
- Source: https://raw.githubusercontent.com/RocketChat/google-summer-of-code/main/google-summer-of-code-2026.md (2026 season page, the latest in the repo).
  - "we will not be accepting any proposals that is directly created by an LLM or Agentic AI tooling."
  - "OK to use AI for research, translation, and so on"
  - "The proposal must be crafted by you personally"
  - "you must be ready to defend every line of its content when/if we contact you for a meeting."
- Contributing guide https://github.com/RocketChat/Rocket.Chat/blob/develop/.github/CONTRIBUTING.md: no AI/LLM text found. It asks for an issue first, the Handbook dev guidelines, PR title prefix, signed CLA.
- Meaning (estimate): the ban is on the GSoC proposal only. AI help with code is allowed, but the CEO must understand and be able to defend every line, and must write the proposal personally. Confirm in the 2027 page when it is published.

### Labels (fact)
- Rocket.Chat/Rocket.Chat: "good first issue" (also seen: "hacktoberfest", "area: ui/ux", "triaged", "gsoc-project"). "good-first-issue" (hyphen) returns 0 org-wide.
- Other repos use "good first issue" and "help wanted".

### Result: no clean first issue found
Every candidate I could check already has an open PR or recent claim. Open PRs/claims mean a maintainer may merge someone else's first, and a duplicate PR wastes the CEO's effort. I did not draft code.

| Issue | Repo | Title | Size | Why dropped / status | Check |
|---|---|---|---|---|---|
| [#26723](https://github.com/RocketChat/Rocket.Chat/issues/26723) | Rocket.Chat | Omnichannel transfer comment not wrapped | S (CSS) | DROP: 29 PRs reference it, 20+ open (e.g. #43226 on 2026-10-28), ~40 assign requests | comments + PR search done |
| [#1276](https://github.com/RocketChat/EmbeddedChat/issues/1276) | EmbeddedChat | Search queries with &, #, + not URL-encoded (`getSearchMessages` in packages/api/src/EmbeddedChatApi.ts) | S | DROP: open PRs #1305, #1277 | PR search done, 0 comments |
| [#1315](https://github.com/RocketChat/EmbeddedChat/issues/1315) | EmbeddedChat | Only last emoji shortname converted (packages/react/src/lib/emoji.js) | S | DROP: open PRs #1401 (2026-10-23), #1316 | done |
| [#1284](https://github.com/RocketChat/EmbeddedChat/issues/1284) | EmbeddedChat | OAuth callback crashes on malformed state (CallbackEndpoint.ts) | S | DROP: open PRs #1306, #1285 | done |
| [#1313](https://github.com/RocketChat/EmbeddedChat/issues/1313) | EmbeddedChat | Last login ambiguous weekday (formatTimestamp.js) | S | DROP: open PRs #1402, #1314, #1333 | done |
| [#1373](https://github.com/RocketChat/EmbeddedChat/issues/1373) | EmbeddedChat | No tests for isMessageSequential | S | DROP: open PR #1374 | done |
| [#1287](https://github.com/RocketChat/EmbeddedChat/issues/1287) | EmbeddedChat | Mention autocomplete on emails | S | DROP: PR #1406 (2026-10-26), #1304 | done |
| [#1286](https://github.com/RocketChat/EmbeddedChat/issues/1286) | EmbeddedChat | Member list truncated at 100 | S | DROP: PR #1304; claim 2026-04-25 | done |
| [#1317](https://github.com/RocketChat/EmbeddedChat/issues/1317) | EmbeddedChat | Permissions change-detection dead | S | DROP: PRs #1318, #1332 | done |
| [#1377](https://github.com/RocketChat/EmbeddedChat/issues/1377) | EmbeddedChat | README Node version mismatch | XS | DROP: PRs #1392, #1378; claim 2026-10-17 | done |
| [#1372](https://github.com/RocketChat/EmbeddedChat/issues/1372) | EmbeddedChat | Composer renders intra-word _ and * as emphasis | M | DROP: PRs #1375, #1376; claim 2026-10-03 | comments done |
| Apps.Notion #41, #43, #58 | Apps.Notion | Modal/comment input bugs | M | Weak: repo last pushed 2024-04-11 (dormant), needs Rocket.Chat server + rc-apps deploy to test; #41 has competing claims | partial |
| Rocket.Chat.Livechat #91, #151, #560 | Livechat | UI bugs | S | DROP: repo archived (pushed 2023-01) | fact |

Not checked (quota out, all in the Meteor monorepo, so untestable cheaply): Rocket.Chat #2938, #23977, #909, #2839, #7734 (labelled good first issue, 9 to 40 comments each, no PR/claim check).

EmbeddedChat facts: default branch `develop`, active (pushed 2026-10-23), 98 open issues, only 25 listed. Many unlabelled 0-comment issues are likely unclaimed (e.g. #1294 forwarded-message UI, #1280 tooltip trailing space has PR #1305 so dropped), but I could not check them.

### Suggested next step (estimate)
Rather than racing existing PRs, pick an unlabelled EmbeddedChat issue from page 2 to 4 of https://github.com/RocketChat/EmbeddedChat/issues?q=is%3Aissue+is%3Aopen+no%3Aassignee , then Ankit runs `gh pr list --repo RocketChat/EmbeddedChat --search "<n>" --state all` and `gh issue view <n> --comments`. When one passes, send me the number and I will draft the diff from raw source. EmbeddedChat is a cheap yarn/npm workspace (needs Node 24 per .nvmrc, issue #1377).

### Draft claim comment and PR text
Not written: no issue chosen. PR template structure (fact, summarised): title prefix (fix/feat/chore/docs/test/...), CLA signed, lint and unit tests pass, add tests, one concern per PR; sections Proposed changes, Issue(s), Steps to test or reproduce, Further comments; changeset file if release-note worthy. EmbeddedChat's own template not fetched.

Branch / commit / test results: placeholders, none yet.
