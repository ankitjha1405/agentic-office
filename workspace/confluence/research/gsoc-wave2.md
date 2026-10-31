---
title: GSoC · Wave 2 First Issues and Tested Local Fixes
owner: coo
contributors: [cto, backend-engineer-1, backend-engineer-2, frontend-engineer-1, frontend-engineer-2, qa-functional]
department: Engineering & Quality
status: Draft
created: 2026-10-31
updated: 2026-10-31
---

# GSoC · Wave 2 First Issues and Tested Local Fixes

Tasks: ENG-12 Oppia, ENG-13 PSF, ENG-14 Sugar Labs, ENG-15 CircuitVerse, ENG-16 MetaBrainz, ENG-17 Learning Equality, ENG-18 Django, ENG-19 AOSSIE. This follows ENG-9/10/11 (`workspace/confluence/research/gsoc-first-issues.md`). Zulip and Rocket.Chat were excluded by the CEO.

Ground rules followed: GitHub was used read-only. No comment, claim, reaction, fork, push, PR or chat post was made anywhere. Clones live only under `/Users/ankitkumar/gsoc-oss/`. All checks were done on 2026-10-31. The CEO (Ankit Jha) reviews, learns and submits every contribution under their own GitHub account, after approval.

## Summary

| Org | AI policy verdict | Clean issue | Fix | Tested | QA |
|---|---|---|---|---|---|
| Oppia | No AI policy found (wiki not fully searched). Assignment by comment required first | None of 17 `good first issue` | None | n/a | n/a |
| PSF (sub-org: holidays) | **Limited**: python-gsoc.org "code you didn't write is not [ok]" (our reading). Skipped by CEO rule | Only #2344, a claimed placeholder | None | n/a | n/a |
| Sugar Labs | Allowed, contributor fully responsible | None. Every musicblocks-v4 starter issue is claimed, has a PR or says "do not start" | None | n/a | n/a |
| CircuitVerse | **Limited**: "AI-generated contributions will not be counted toward Google Summer of Code (GSoC)"; PR text must be your own. Skipped | None of ~24 anyway | None | n/a | n/a |
| MetaBrainz | **Limited**: "We discourage the use of AI tools in communications and contributions." Skipped | Not searched further (stopped at policy) | None | n/a | n/a |
| Learning Equality | Allowed ("welcome to use generative AI"), but no PR without assignment | None: 20 of 21 `help wanted` assigned | None | n/a | n/a |
| Django | Allowed with disclosure; no AI reviews on PRs | None found: Trac list pages return 403 to our tools, 12 single tickets checked, none free | None (clean clone of main only) | n/a | n/a |
| AOSSIE | Allowed with disclosure | **Template-Repo #73** | `gsoc/73-dependabot-groups` @ `17818ef` | **Partly**: YAML parse passed; Dependabot behaviour UNTESTED (only GitHub can run it) | Divya: accept with notes |

**Result: 1 fix out of 8 orgs.** Three orgs were skipped on policy (PSF, CircuitVerse, MetaBrainz). Four had no clean newcomer issue today (Oppia, Sugar Labs, Learning Equality, Django). As in wave 1, labelled newcomer issues get claimed within days, and most of these orgs want you to be assigned (by comment or chat) before you start. Neither of those is something we can do under the read-only rule.

**Tooling limits in this session (fact):** `gh` read, `git clone/switch/add/commit` via `git -C`, `python3` stdlib, `node`, `npx` worked. `pip`, `npm install`, `uv`, `ruby`, `curl` and some `gh api` calls were denied. Nothing was worked around.

### What would unlock more fixes (CEO actions, each needs your own account)
1. **Django:** open https://code.djangoproject.com/query?status=!closed&easy=1&stage=Accepted&owner=nobody in a browser and send 2 or 3 ticket numbers. Aditya then runs the checks and drafts. Clone ready at `/Users/ankitkumar/gsoc-oss/django`.
2. **Sugar Labs / Oppia / Learning Equality:** these orgs assign first. You ask for an issue in your own words; once assigned, we draft.
3. **MetaBrainz / CircuitVerse / PSF:** write those contributions yourself, without AI-drafted code. CircuitVerse would not count AI-drafted work for GSoC anyway.

### Before submitting anything (every time)
1. Open the issue and read the last 10 comments.
2. In the repo's Pull requests tab, search `is:pr is:open <issue number>`.


## AOSSIE (Template-Repo issue #73)

Checked 2026-10-31 by Nikhil Bhatt (ENG-19). GitHub was used read-only. Nothing was posted anywhere.

### Policy

Org policy: https://github.com/AOSSIE-Org/Info/blob/main/Rules/AI.md . I read it again from the raw source (WebFetch). My tool caps verbatim quotes, so these are close paraphrases, except the one quote that wave 1 already recorded.
- Exact quote (from wave 1): "AI is your tool. You are not AI's tool."
- AI is accepted for communication, research, brainstorming, generating code, PR descriptions and review.
- Disclose AI-generated ideas and solutions, including in chat and GSoC proposals.
- "Test AI-generated code locally before submitting a PR."
- If a PR has AI-generated code, add a short paragraph saying which models you used and how (the PR template has a section).
- Address CodeRabbit comments before asking for human review. Low-effort AI messages, issues or PRs can lead to bans.
- Individual projects may add their own AI-UsagePolicy.md that extends or overrides it.

Repo check: Template-Repo has NO AI-UsagePolicy.md (I listed the repo root, `.github/` and globbed for the name). Its own rules:
- https://github.com/AOSSIE-Org/Template-Repo/blob/main/CONTRIBUTING.md : "We accept the use of AI-powered tools (GitHub Copilot, ChatGPT, Claude, Cursor, etc.) for contributions, whether for code, tests, or documentation." and "if you use AI assistance, please mention it in your PR description."
- Same file: "PRs without Discord updates will not be reviewed or may face delays." and "Wait to be assigned before starting work(preferable)". Branch rule: new branch, never on main/dev. Commits are conventional (`feat:`, `fix:`).
- PR template AI notice: "Submissions that do not meet these standards may be closed without warning".

Verdict: AI-written code is ALLOWED with disclosure. No ban, no limit on using AI to find work. Proceeded.

### Issue

https://github.com/AOSSIE-Org/Template-Repo/issues/73 "[FEATURE]: consider groups or multi-ecosystem-groups in dependabot.yml". Labels: enhancement, help wanted, ci-cd, good-first-issue, dependencies. (Note the label is spelled `good-first-issue` with hyphens in this repo.)

### Why it is free

- Assignees: none (`gh issue view 73 --json assignees` returned `[]`). State OPEN.
- PR search: `gh pr list --repo AOSSIE-Org/Template-Repo --search "73" --state all` returned #87 and #86 (both from kallal79, both CLOSED; #87 auto-closed as stale on 2026-03-26 after no activity) plus unrelated PRs. `closedByPullRequestsReferences` is `[]`. `gh pr list --search "dependabot" --state open` shows only 3 bot version-bump PRs (#168 to #170), none for this issue. Open PR #167 touches 18 files, none is dependabot.yml.
- Comments (5): claims on 2026-02-21, 02-22, 03-03, 03-21, and one non-claim comment by m13v on 2026-09-09 (a remark about trade-offs of groups). No claim since 2026-09-01. Nobody was ever assigned.
- Weak points: the issue says "consider", so a maintainer may still say no. Four people asked to be assigned in Feb to Mar and were never answered. Maintainer is kpj2006.

### Local path

/Users/ankitkumar/gsoc-oss/Template-Repo

### Branch

`gsoc/73-dependabot-groups` (the repo asks for a new branch, not main; local only, not pushed)

### Commit

`17818ef feat(dependabot): group version updates per ecosystem (#73)`

### Test command and output

The repo has no tests for this file. I checked that the edited file is valid YAML and that each of the 13 `updates` entries parses with a `groups` block, using `npx --yes js-yaml /Users/ankitkumar/gsoc-oss/Template-Repo/.github/dependabot.yml`. It parsed with exit 0. Last lines of the output:

```
      "labels": [
        "dependencies",
        "dotnet"
      ],
      "commit-message": {
        "prefix": "chore(deps)",
        "include": "scope"
      },
      "pull-request-branch-name": {
        "separator": "-"
      }
    }
  ]
}
```

That is a syntax check only. UNTESTED against real Dependabot: only GitHub can run Dependabot, and its parser may behave differently. The Dependabot "groups / patterns" keys are the documented standard form (docs.github.com Dependabot options reference lists `groups`, `patterns`, wildcards), but I did not see Dependabot accept this file. `pre-commit` is not installed here, so the repo's hooks were not run.

Git output after the commit:

```
$ git -C .../Template-Repo log --oneline -3
17818ef feat(dependabot): group version updates per ecosystem (#73)
ace6306 Add AI Moderator workflow for issue management
4808818 Rename workflow from PR Quality to Anti Slop PR

$ git -C .../Template-Repo status --short
(empty)

$ git -C .../Template-Repo diff HEAD~1 --stat
 .github/dependabot.yml | 41 +++++++++++++++++++++++++++++++++++++++++
 1 file changed, 41 insertions(+)
```

### Changed lines explained

Only `.github/dependabot.yml`, 41 added lines, none removed.
- Lines 11 to 12: two comment lines under customization step 4. They tell template users that updates are now grouped, and how to turn it off (delete `groups`).
- 13 times, one per ecosystem (npm, github-actions, docker, bundler, cargo, maven, gradle, composer, gomod, pip, terraform, pub, nuget): a `groups:` block with one group named after the ecosystem and `patterns: ["*"]`. In plain English: "put every dependency of this ecosystem into one group". Dependabot then opens one PR per ecosystem for version updates instead of up to 5 separate PRs. So the worst case drops from 5 x 13 = 65 open PRs to 13. Security updates are not grouped (the default applies to version updates only), so they still arrive alone.
- Nothing else changed: schedule, labels, commit prefix and limits are the same.

```diff
diff --git a/.github/dependabot.yml b/.github/dependabot.yml
index af82e93..aa42116 100644
--- a/.github/dependabot.yml
+++ b/.github/dependabot.yml
@@ -10,0 +11,2 @@
+#    Each ecosystem uses "groups" so all its version updates arrive in one PR
+#    (at most one PR per ecosystem). Remove "groups" to get one PR per dependency.
@@ -32,0 +35,3 @@ updates:
+    groups:
+      npm:
+        patterns: ["*"]
@@ -49,0 +55,3 @@ updates:
+    groups:
+      github-actions:
+        patterns: ["*"]
@@ -67,0 +76,3 @@ updates:
+    groups:
+      docker:
+        patterns: ["*"]
@@ -85,0 +97,3 @@ updates:
+    groups:
+      bundler:
+        patterns: ["*"]
@@ -103,0 +118,3 @@ updates:
+    groups:
+      cargo:
+        patterns: ["*"]
@@ -121,0 +139,3 @@ updates:
+    groups:
+      maven:
+        patterns: ["*"]
@@ -139,0 +160,3 @@ updates:
+    groups:
+      gradle:
+        patterns: ["*"]
@@ -157,0 +181,3 @@ updates:
+    groups:
+      composer:
+        patterns: ["*"]
@@ -175,0 +202,3 @@ updates:
+    groups:
+      gomod:
+        patterns: ["*"]
@@ -193,0 +223,3 @@ updates:
+    groups:
+      pip:
+        patterns: ["*"]
@@ -219,0 +252,3 @@ updates:
+    groups:
+      terraform:
+        patterns: ["*"]
@@ -237,0 +273,3 @@ updates:
+    groups:
+      pub:
+        patterns: ["*"]
@@ -256,0 +295,3 @@ updates:
+    groups:
+      nuget:
+        patterns: ["*"]
```

(The diff above is `git diff HEAD~1 -U0`, shortened context. Unified default context gives the same additions.)

### Draft PR description

Follows https://github.com/AOSSIE-Org/Template-Repo/blob/main/.github/PULL_REQUEST_TEMPLATE.md . Checkboxes left unticked for the CEO.

```
### Addressed Issues:
Fixes #73

### Screenshots/Recordings:
Not applicable (config change).

### Additional Notes:
Adds a `groups` block (`patterns: ["*"]`) to each of the 13 ecosystems in `.github/dependabot.yml`, so version updates for one ecosystem arrive as one PR. Worst case drops from 5 PRs x 13 ecosystems = 65 to 13. Security updates are not grouped. I chose per-ecosystem `groups` over `multi-ecosystem-groups` because it is the long-standing documented form and keeps the existing per-ecosystem labels and commit prefix. Trade-off: a grouped PR can hide one dependency that failed to resolve, so CI should be read before merging. If maintainers prefer a single PR across all ecosystems, I can switch to multi-ecosystem-groups.

AI assistance: I used Claude (Anthropic) to help find this issue, read the Dependabot docs and write the YAML edit. I reviewed every line, checked the file parses as valid YAML with `npx js-yaml`, and understand each change. I could not run Dependabot itself, so I will watch the first Monday run after merge.

## Checklist
- [ ] My code follows the project's code style and conventions
- [ ] I have made corresponding changes to the documentation
- [ ] My changes generate no new warnings or errors
- [ ] I have joined the Discord server and I will share a link to this PR with the project maintainers there
- [ ] I have read the Contributing Guidelines

## ⚠️ AI Notice - Important!

We encourage contributors to use AI tools responsibly when creating Pull Requests. While AI can be a valuable aid, it is essential to ensure that your contributions meet the task requirements, build successfully, include relevant tests, and pass all linters. Submissions that do not meet these standards may be closed without warning to maintain the quality and integrity of the project. Please take the time to understand the changes you are proposing and their impact.
```

### QA (qa-functional, Divya, 2026-10-31)
ACCEPT WITH NOTES. `git diff HEAD~1` matches the diff above exactly (one file, 41 lines added, none removed). Divya re-ran `npx --yes js-yaml` on the file: exit 0, 13 `groups` blocks, each with `patterns: ["*"]`. The Dependabot options reference lists `groups` / `patterns` with `*` wildcards; no conflict with `open-pull-requests-limit` was found (only the first 100k characters of the page were read). Re-check of the issue today: OPEN, no assignee, newest comment 2026-09-09 (not a claim), no open PR for "73". Fix applied by Ankit: the template's "AI Notice" section was missing from the PR draft and has been restored. Not proven on live Dependabot.

Before the PR the CEO must: join the AOSSIE Discord, say in the project channel that they want to take #73, and preferably wait to be assigned (CONTRIBUTING.md). Re-check the issue for new claims or PRs on the day. The CEO writes any chat message themselves. If they use AI for the idea or text, they must say so.

### Risks / open questions

- Maintainer fit: the issue says "consider", and the only post-March comment warns that grouping can hide failures. A maintainer may prefer multi-ecosystem-groups or no change. Ask in Discord first.
- Not proven on real Dependabot (YAML syntax check only). Also the issue says "14 ecosystems"; the file has 13 entries. I did not add a fourteenth.
- No pre-commit run (not installed). The repo CI has an "Anti Slop PR" workflow and CodeRabbit; expect automated review comments to answer.
- The 4 earlier claimants (Feb to Mar) were never assigned, but may return. Check again the day you start.
- This is a template repo, so the learning value is lower than for a product repo. It is the only unassigned `good first issue`-style item left in the org that was not already rejected and has no open PR.
- Everything else with the label in AOSSIE is assigned (PictoPy, Resonate, CarbonTracker, BabyNest, Monumento) or already rejected in wave 1.

### Candidates checked

| Candidate | Result |
|---|---|
| Template-Repo #73 | CHOSEN. Open, unassigned, label good-first-issue, no open PR, last claim 2026-03-21 |
| Devr.AI #93 | Rejected: 5+ open PRs mention it (#191, #187 and others), 15 comments, many claims, last 2026-01-29 |
| Template-Repo #16 | Skipped: "ideas welcome" discussion, not a fix |
| SocialShareButton #94 | Skipped: record a tutorial video, not code |
| SocialShareButton #19 | Skipped: has assignee, tutorial task |
| Resonate #488 | Skipped: translations, 54 comments, many languages split among people |
| PictoPy (#1647, #1645, #1460, #966, #939, #803, #705, #636), Resonate (#729, #711, #710, #704, #680, #628, #623, #604, #587, #574, #555), Resonate-Backend #140, CarbonTracker #18, BabyNest #287, Monumento #178 | Rejected: each has an assignee |
| EduAid #34 | Skipped: feature (audio input), 25 comments, not small |
| OpenPeerChat-flutter #27 | Skipped: feature (export chat), needs Flutter toolchain, 9 comments |
| OrgExplorer open bugs (#375 to #433, about 25) | Not used: no newcomer label (only `bug`), and wave 1 already rejected several. Not checked for claims |
| Already rejected in wave 1 (EduAid #592/#603/#668/#69, DebateAI, Perspective, Skills #8, Agora, OpenVerifiableLLM, Rein, OrgExplorer) | Not re-checked as instructed |

Count: about 12 distinct candidates examined in detail or by list, plus the assigned-issue sweep from one `gh search` call.

## Django

**Result: no clean issue. No branch, no commit, no draft PR.** The Trac ticket list could not be read, and every ticket I could reach was closed or claimed.

### Policy
Source: https://docs.djangoproject.com/en/dev/internals/contributing/writing-code/submitting-patches/ (section "AI-Assisted Contributions"). I re-checked the quotes against the cloned file `/Users/ankitkumar/gsoc-oss/django/docs/internals/contributing/writing-code/submitting-patches.txt`, lines 155-200.

- "Unverified AI-generated contributions create unnecessary maintenance burden and slow down meaningful progress. Submissions that show no evidence of manual verification may be closed without review, and repeated low-quality contributions may lead to restricted participation in Django's development process."
- "If you use AI tools while preparing a contribution, you must: **Disclose** which AI tools were used and what they were used for ... **Review and verify** all AI-generated output ..."
- "Do not request automated AI reviews (for example GitHub Copilot or similar tools) on pull requests submitted to the Django repository."
- "Note for AI Tools: ... Disclose your involvement ... Include the name and version of the AI tool ... Follow the GitHub pull request template."

**Verdict:** AI help is allowed with disclosure and human verification. It is not banned or materially limited, so the stop rule does not apply. The CEO must disclose the tool and what it did, and must not request Copilot or other AI reviews on the PR.

Claiming rule (same page): tickets must be "Accepted" and "Owned by" nobody. Small fixes need no claim.

### Issue
None found. See "Candidates checked".

### Why it is free
Not applicable.

### Local path
`/Users/ankitkumar/gsoc-oss/django` is cloned (depth 50, on `main`, untouched). asgiref and sqlparse were not cloned.

### Branch / Commit / Test command and output / Changed lines / Draft PR description
None. Nothing was written or tested.

### Risks / open questions
- **Blocker:** `code.djangoproject.com/query?...` (and `format=csv`, `format=rss`, `/timeline`) returned HTTP 403 to WebFetch every time. `/report/` returned 404. I did not try to get around the 403, for example with curl. Only single ticket pages (`/ticket/N`) could be read.
- The django-updates mail archive (mail-archive.com) shows nothing newer than mid-June 2026. Tickets exist up to at least #37463, since the Django repo has "Fixed #37463" dated 2026-10-28. Tickets from July to October are invisible to me.
- Easy tickets on Django are claimed within hours (#37062, #37080, #37088, #37178 each had an owner and a PR within a day). A list that is days old would be stale anyway.
- Suggested next step: the CEO (a human, in a browser) opens https://code.djangoproject.com/query?status=!closed&easy=1&stage=Accepted&owner=nobody and gives me 2-3 ticket numbers. I will then run the PR search and the claim check, and do the fix. Alternatively, drop Django from wave 2.
- Django wants a regression test, and a release note only for backward-incompatible changes or stable-branch backports. It also wants a single squashed commit titled "Fixed #NNNNN -- ...".
- Tests would need asgiref and sqlparse cloned into `_deps` first.

### Candidates checked
All read-only from Trac ticket pages on 2026-10-31. I did not run the `gh pr list` check because none passed the first filter.

| Ticket | Title | State | Why rejected |
|---|---|---|---|
| #37179 | Slicing a GDAL layer should scan layer once only | closed needsinfo | Closed, owner wongcht, stage Unreviewed |
| #37176 | Action importable from django.contrib.admin | closed fixed | Closed, not easy |
| #37178 | Move MiddlewareMixin out of utils.deprecation | closed fixed | Closed, claimed, PR #21519 |
| #37125 | Use `__new__` to sanitize TaskResult | closed invalid | Closed, owner zky |
| #37088 | path based MediaAsset equality | closed fixed | Closed, owner Johannes Maron |
| #37080 | Deprecation warnings as errors in tests | closed fixed | Closed, PR #21216 |
| #37062 | preserve_request in RedirectView | closed fixed | Closed, PR #21167 |
| #29260 | Remove UPDATE on new instance with pk default | closed fixed | Closed, not easy |
| #28223 | Form not picklable (template renderer) | assigned | Owner Ishan Kumar, PR #22153 (Oct 14, 2026) |
| #9270 | Docs: FORCE_SCRIPT_NAME syntax | closed fixed | Closed in 2013 |
| #33685 | Service names for PostgreSQL tests | assigned | Owner Pravin, has patch, not easy |
| #37460 | Second new contributors tutorial | closed | Not easy, no owner, but closed (needsnewfeatureprocess) |
| #37470, #37466 | (probes) | 404 | Do not exist yet |

## Oppia

**Result: NO CLEAN ISSUE. No clone, no branch, no commit, no draft.** Date checked: 2026-10-31.

### Policy
- No AI/LLM policy found. I read the `.github` folder listing, `CONTRIBUTING.md` (https://github.com/oppia/oppia/blob/develop/.github/CONTRIBUTING.md), and the wiki pages "Contributing code to Oppia" (https://github.com/oppia/oppia/wiki/Contributing-code-to-Oppia) and "Rules for making PRs" (https://github.com/oppia/oppia/wiki/Rules-for-making-PRs). None mention AI, LLM or generative tools. Caveat: the wiki has about 137 more pages I could not list, and the page fetcher summarises text, so a policy elsewhere is not ruled out. Verdict: no ban found, but unconfirmed. CEO should do a quick wiki search for "AI" before any PR.
- Assignment is required before starting. Quotes from the Contributing page:
  - "Once you have a good understanding of the issue, you can ask for it to be assigned to you by leaving a comment as follows:"
  - "Once assigned, feel free to submit a PR and get it merged"
  - "Please only work on issues that are labelled "Impact: High" or "Impact: Medium", and that have no assignee."
  - "Do not work on "Impact: Low" or "Backlog" issues." and "Do not work on issues with the "triage needed" label"
  - "If you do not sign the CLA, any PRs you open will be closed."
- Asking for assignment means posting a comment. That is forbidden for me under the brief, so the CEO would have to do it.

### Issue
None selected. Label used: "good first issue" (17 open, unassigned in GitHub's assignee field, found with `gh issue list --repo oppia/oppia --label "good first issue" --state open --no-assignee`).

### Why none is free
Oppia assigns by maintainer comment, so the assignee field is empty even on issues that are effectively claimed. Almost every issue has claim or assignment traffic since 2026-09-01. The rest need the full GAE/Karma/Playwright stack, which cannot run here (no npm/pip install, no Docker).

### Candidates checked
| # | Title (short) | Last activity | Finding | Verdict |
|---|---|---|---|---|
| 26843 | Playwright migration voiceover-admin | 2026-10-17 | 2026-10-17 contributor asked, maintainer said "you can work on it" (effectively claimed) | Not free |
| 26842 | Playwright migration translation-submitter | 2026-10-16 | Active PR review thread 2026-09-22 to 09-24 | Not free |
| 26838 | Playwright migration site-moderator | 2026-10-29 | Updated 2 days ago, 13 comments; not read in detail | Not free (active) |
| 26832 | Playwright migration logged-in-user | 2026-10-25 | 22 comments, active; not read in detail | Not free (active) |
| 26828 | Playwright migration interested-parent | 2026-10-28 | 48 comments, active; not read in detail | Not free (active) |
| 26799 | Playwright migration exploration-creator | 2026-10-31 | Updated today | Not free (active) |
| 25612 | Sync LC.1 CUJ with acceptance tests | 2026-10-15 | 2026-10-13 request, 2026-10-15 maintainer "not assigned, open"; contested | Not free; also Playwright |
| 23496 | Enforce strict type checks | 2026-10-06 | 2026-10-05 reply "all groups assigned to others" | Not free |
| 21970 | Missing domain objects `validate()` | 2026-10-30 | Checkbox issue, claims and assignments 2026-10-27/28 | Not free; needs GAE |
| 21308 | Cover all backend branches with tests | 2026-10-28 | Checkbox issue, claims and assignment 2026-10-27/28 | Not free; needs GAE |
| 8015 | Backend API service returns domain object | 2026-10-28 | Checkbox issue, assignment 2026-10-28 | Not free |
| 12912 | Fix pylint problems | 2026-10-31 | Contributor actively working with maintainer 2026-10-29 to 10-31 | Not free |
| 12238 | Sticky question in review modal | 2026-02-21 | Repeated claims and pings, past PRs reverted for regression; Angular UI, Karma | Not free, risky |
| 18422 | Prerequisite skill not shown | 2026-04-28 | Many "cannot reproduce" comments; maintainer could not reproduce | Not suitable |
| 18876 | Concept card bug | 2026-10-30 | 32 comments, updated 1 day ago; not read in detail | Not free (active) |
| 20392 | Exploration preview tab | 2026-10-30 | 79 comments, active; UI work | Not free (active) |
| 18470, 5670 | Classroom admin UX; sortable skills list | 2026-03-13, 2026-06-19 | Large UI features (Work: Medium/High), need Karma/GAE | Not suitable |

Not one is a pure TS or Python helper testable with `node --test`, stdlib unittest or a standalone vitest harness. I did not read every comment on the last six rows; they are rejected on activity dates and test-stack grounds (this is a judgement, not a full comment audit).

### Local path / Branch / Commit / Tests / Diff / Draft PR
None. Nothing cloned or run. Tests: not applicable (UNTESTED, nothing built).

### Risks / open questions
- Tooling note: `gh api` calls were denied by the session permission layer, so I used `gh issue view --json comments` and `gh issue list` instead. No work-around attempted.
- Wiki AI policy not fully confirmed (see Policy).
- Suggestion: Oppia is a poor fit for a one-shot, in-session fix. If the CEO wants Oppia anyway, the realistic route is to join GitHub Discussions, pick a Python `core/domain` checkbox item, and get assigned first. That needs the GAE dev setup on a machine with install rights.

## Python Software Foundation (sub-org: Open World Holidays Framework, vacanza/holidays)

**Result: STOPPED at step 1 (policy). No clone, no branch, no commit, no draft. Nothing was posted anywhere.**

### Policy

PSF umbrella guidance, https://python-gsoc.org/ (Getting Started, "patch" section):
- "Usually we expect GSoC contributors to fix a bug and have made a pull request (or equivalent)."
- "Your code doesn't have to be accepted and merged, but it does have to be visible to the public"
- "it does have to be your own work (mentor help is ok, code you didn't write is not)."

The PSF pages (https://python-gsoc.org/, /contributors.html, /ideas.html) have no explicit AI or LLM policy. The nearest text is "If you want to work on generative AI, LLMs, crypto, machine learning, big data, etc", which is about project topics, not authorship.

Google GSoC 2026 guidance, https://developers.google.com/open-source/gsoc/resources/ai_guidance:
- "The human contributor retains 100% responsibility for the work."
- "Use AI tools mostly for research and less for code generation."
- "Always be sure to verify directly with your org if they allow AI generated code in their code base."

Chosen sub-org (vacanza/holidays) own docs: CONTRIBUTING.md (https://raw.githubusercontent.com/vacanza/holidays/dev/CONTRIBUTING.md) and https://holidays.readthedocs.io/en/latest/contributing/ have no AI or LLM text. The PR template (.github/PULL_REQUEST_TEMPLATE.md) has no AI disclosure line. I found no AI policy file in the repo (one guessed path returned 404; GitHub contents API was blocked in this session, so I could not list .github).

**Verdict: STOP.** PSF says "code you didn't write is not [ok]" and Google says to verify AI-generated code with the org first. Holidays is silent, so permission is not confirmed. Under brief step 1 ("banned or materially limited") the safe reading is that a Claude-written patch under the CEO's name is not allowed until a maintainer says it is. This is a judgement call; see Decisions below.

### Issue

None selected. The only open issue with the label "good first issue" in vacanza/holidays is #2344, "Localize untranslated `.po` files" (https://github.com/vacanza/holidays/issues/2344). It is not usable even if policy allowed.

### Why it is free

It is not free. Evidence from `gh issue view 2344 --repo vacanza/holidays --comments` (run 2026-10-31):
- Maintainer KJhellico/arkid15r call it "a placeholder issue, please create one related to localization you'd like to work on."
- About 25 "I wish to work on this / assign me" comments, many tagged GSoC 2026 applicants. Recent claims include Sandeep-kumar15 (Hindi for Oman) and AdityaPandji (Hindi for Bahrain), both told "go for it" by maintainer PPsyrius, plus ahmershahdev (Urdu Gulf states, PRs #3864-3873 merged or open).
- Maintainers say open a new issue per locale first, to avoid duplicate work.
- Related #3065 was named as beginner-friendly but is already assigned to several people (per a comment in #2344).
- I did not run the PR search because the issue failed the claim check.

### Local path
None (no clone).

### Branch
None.

### Commit
None.

### Test command and output
Not run. No code written.

### Changed lines explained
None.

### Draft PR description
None. If a maintainer later approves AI help, the PR template has: Proposed change, Type of change (pick one of ten), Checklist (read contributing guide, `make check` passes). Disclosure line would be: "I used Claude (Anthropic) to help ...; I reviewed every line and ran the tests myself."

### Risks / open questions
- Strictness of "code you didn't write is not [ok]" is my reading, not a PSF ruling. CEO may decide it only covers copying other people's code and that AI-assisted code the CEO reviews and owns is fine.
- Holidays is the only PSF sub-org with pure Python plus pytest. Others fail the rule: MNE-Python, DIPY, FURY, ilastik need numpy/scipy/compiled code, pocketpy is C11, Pwndbg needs a debugger, Vorta (Borg Collective) needs Qt.
- Holidays also needs `uv` and `make setup`, which are blocked here; tests might need manual PYTHONPATH work (python-dateutil is a runtime dep).
- Holidays is a very crowded newcomer target (GSoC 2026 applicants swarm it), and a holidays-data fix needs official-source evidence.

Option for CEO: ask a holidays maintainer, in the CEO's own words, whether AI-assisted patches are acceptable (I must not post this). If yes, I can look for a fresh non-l10n issue (unlabelled ones, or financial-holiday gaps) in a new task.

### Candidates checked

| Item | Result |
|---|---|
| PSF python-gsoc.org guidance | "code you didn't write is not [ok]", no AI policy |
| Google AI guidance | verify with org first |
| vacanza/holidays CONTRIBUTING + docs | no AI policy |
| #2344 (only "good first issue" open) | placeholder, ~25 claims, fails |
| #3065 | assigned to several people per #2344 comments, not opened |
| Other 7 sub-orgs | not pure Python or have C/Qt deps, not examined for issues |

## Sugar Labs

**Result: NO CLEAN ISSUE. No clone, no branch, no commit, no draft PR. Nothing was written to any repo.**

### Policy

AI-assisted work is allowed, so the policy is not the blocker. Source: https://github.com/sugarlabs/musicblocks/blob/master/CONTRIBUTING.md (section "Using AI/LLM tools for code changes"; the musicblocks-v4 repo points to the same rules). I could only read it through a summarising fetch tool that caps quotes at 125 characters, so the quotes below are short fragments, not full sentences.

- "contributors remain fully responsible for any code they submit."
- "Avoid submitting large AI-generated patches without manual review."
- "Mentioning AI assistance in your pull request description is optional but encouraged"
- Tools named in the guide include GitHub Copilot, ChatGPT, Cursor and Claude.
- Also from the guide: do not submit code you cannot explain and maintain; do not submit unrelated AI-suggested changes; run lint, format and tests first; mind licensing.
- Commit rules: Conventional Commit title (`<type>: <subject>`), every commit needs a `Signed-off-by` trailer (`git commit -s`, CI enforced), and "Mention an issue number in the pull request, but not the commit message."

Verdict: AI help is permitted with full human review. Not banned. Not checked: the sugarlabs/.github repo and the www-sugarlabs/GSoC pages (the `gh api` read was denied in this session, so I could not list them). A code search of the org found only the musicblocks CONTRIBUTING and sugarlabs/docs `src/contributing.md` mentioning LLMs; I could not fetch the latter (404 on the path I guessed).

### Issue

None qualifies. Why: Music Blocks (the CTO's pick) has no "good first issue" label in use (`gh issue list --repo sugarlabs/musicblocks --label "good first issue"` returned `[]`). Sugarizer has issues disabled (`gh` said: "the 'sugarlabs/sugarizer' repository has disabled issues"). The newcomer label exists only in other repos, mainly `sugarlabs/musicblocks-v4` (TypeScript/React/vitest, "Good for new contributors"). Every open, unassigned one there fails the brief's rules (table below).

### Why it is free

Not applicable (no issue chosen). Two points matter for the CEO:

1. Every v4 "good first issue" body ends with: "Please do not start work on this issue until it has been assigned to you. Comment to ask for it first." The brief forbids commenting, so no v4 issue can be done under these rules. Even a perfect fix would break the maintainers' stated process.
2. The free-looking ones are heavily claimed. #876 has a linked PR (#916 by a contributor, per comments) plus 4 claim comments; #878 has 8 claim comments, the latest on 2026-10-29.

### Local path
None.

### Branch
None.

### Commit
None.

### Test command and output
None run. UNTESTED, because there is no fix.

### Changed lines explained
None.

### Draft PR description
None. If the CEO wants to pursue Sugar Labs anyway, the PR would need: Conventional Commit title, `git commit -s`, issue linked in the PR body only, and an AI disclosure ("I used Claude (Anthropic) to help ... I reviewed every line and ran <tests> myself"). The CEO would first have to ask for assignment on the issue, in their own name.

### Risks / open questions

- Decision for the CEO: ask for assignment on a v4 issue personally (their comment, their account), or drop Sugar Labs in wave 2. Candidates worth asking about: #888, #887, #886, #885, #883, #882, #881, #880 (label "help wanted", not "good first issue", unassigned, updated in Oct). None checked for claims or PRs, and "help wanted" is not the newcomer label, so I did not count them.
- Sugar Labs mentors say new people should ask first; a speculative PR may be closed (one v4 comment says a PR was "closed, rightly" for skipping the queue).
- Some v4 comments are AI-generated spam with payout addresses (#877, #878). Ignore them; they are not guidance.
- Sugar Labs is crowded: v4 starter issues attract several claims within days.

### Candidates checked

All "good first issue" unless noted. Checked 2026-10-31 with `gh issue view <n> --comments`. Claim cutoff 2026-09-01.

| Issue | Title (short) | Result | Reason |
|---|---|---|---|
| v4 #876 | Snap distance ignores zoom | FAIL | PR #916 open (per comments), 4 claims since Sep 22, latest Oct 6 |
| v4 #877 | Stale Palette doc comment | FAIL | Claims Sep 22 and Oct 23; member said docs issues are mislabeled and planned elsewhere |
| v4 #878 | Remove unused deps | FAIL | 8 claim comments, latest Oct 29; needs npm install and CI change |
| v4 #868 | Bricks stay selected after drag | FAIL | Closed by PR #871 per comments, was assigned |
| v4 #628 | Tight padding in path utility | FAIL | "Do not work on this until marked ready." |
| v4 #685 | Palette tooltip | FAIL | "Do not work on this until marked ready." |
| v4 #679 | Palette styling | FAIL | Claims Jul 31 and Sep 14 (Sep 14 is inside the window); styling, not testable logic |
| v4 #678 | Masonry QoL parent | FAIL | Parent issue, PRs go to sub-tasks |
| v4 #631 | Brick design evaluation | FAIL | Design evaluation, 4 comments, not a small fix |
| www-v2 #1084 | Sweet Spot tag in search | FAIL | Claims Oct 20 and Oct 22, a PR #1093 is mentioned in comments |
| musicblocks (main) | all open issues | FAIL | No newcomer label in use |
| sugarizer | all | FAIL | Issues disabled |
| v4 #874 to #875, #873, #872, #842, #841, #830, #820, #814, #811, #810, #808 | various | FAIL | Assigned to a user (seen in the search listing only, not opened) |
| v4 #681 | Pie menu widgets | NOT OPENED | Listed unassigned, same "TBD" pattern as #628 and #685 but I did not read it |
| aslo-v4 #71, ordinals-activity #1 | UX complaint, discard card | NOT OPENED | Stale (2024, 2019); Python/GTK or non-pure-function, out per CTO |

Limits: `gh api` and `gh label list` were denied by the session, so the label inventory comes from `gh search issues` and `gh issue list` only.

## CircuitVerse

**Result: STOPPED. No clone, no branch, no commit, no draft PR.** Two independent reasons: (1) the AI policy materially limits this work, (2) no clean issue exists.

### Policy
Source: cv-frontend-vue CONTRIBUTING.md, section "AI Assistance Policy" (https://github.com/CircuitVerse/cv-frontend-vue/blob/main/CONTRIBUTING.md). The main Rails repo CONTRIBUTING.md (https://github.com/CircuitVerse/CircuitVerse/blob/master/CONTRIBUTING.md) has no AI policy. Quotes below came from two WebFetch passes of the cv-frontend-vue file (the tool summarises, so wording is short quotes, not a full verbatim copy):

- "You may use AI assistance under these conditions:"
- "Read and understand every line of code before submitting it."
- "Verify the change by running it in the development environment."
- "Write issue and pull request titles and descriptions yourself, following the issue/pull request templates"
- "Fill out the AI-assistance section of the pull request template honestly."
- "AI-generated contributions will not be counted toward Google Summer of Code (GSoC)."

Other rules: commits follow Conventional Commits, format `<type>: <description> (#issue-number)`; "Find an issue without the pending triage label"; "Start working immediately, no need to wait for assignment".

**Verdict: materially limited, STOP.** AI code is allowed, but (a) AI-generated contributions explicitly do not count toward GSoC, which is the whole purpose of this task, and (b) the PR title and description must be written by the contributor, so I cannot supply a draft PR description. Submitting AI-written work for GSoC credit would also run against the stated rule.

### Issue
None selected.

### Why it is free
Not applicable. Evidence that the pool is also not clean is in the table below.

### Local path / Branch / Commit
None. Nothing cloned, nothing created.

### Test command and output
None run (UNTESTED, because no code was written).

### Changed lines explained
None.

### Draft PR description
None. The policy requires the contributor to write it.

### Risks / open questions
- Decision for the CEO: if the goal is real GSoC credit for CircuitVerse, the code and PR text must be human-written. AI may at most help understand the code. I suggest dropping CircuitVerse from the AI-drafted wave and picking it up by hand later.
- Even by hand, the cv-frontend-vue newcomer pool is crowded: almost every open `good first issue` already has an open PR (see table). Check again before starting; new typecheck or TypeScript-conversion issues appear in batches (many were filed 2026-10-13).
- The 60-day claim window runs from 2026-09-01.

### Candidates checked
Commands: `gh search issues --owner CircuitVerse --label "good first issue" --state open`, `gh issue view N --comments`, `gh pr list --repo CircuitVerse/cv-frontend-vue --state all --search ...`. All repos are cv-frontend-vue unless noted.

| Issue | Problem |
|---|---|
| #1405 Ground + Power to TS | Open PR #1444; claim comment |
| #1406 Clock + Dlatch to TS | Open PR #1442 |
| #1407 ForceGate to TS | Open PR #1425 |
| #1409 LSB + MSB to TS | Claim by pantha704, open PR #1448 |
| #1410 Logo/TextEditor lang=ts | Open PR #1430 |
| #1411 RestrictedElementNotice | Claimed/queried 2026-10-13 and 2026-10-19; already covered by PR #1293 per comments |
| #1412 jQuery out of dialogs | Open PR #1424 |
| #1414 widen id types | Open PR #1435 |
| #1415 DeleteCircuit cast | Open PR #1434 |
| #1416 propagationDelay | Open PR #1461 |
| #1417 CustomShortcut types | Open PRs #1432, #1479 |
| #1418 SimulationArea | Open PR #1433 |
| #1419 Node shape | Open PR #1462 |
| #1420 one-line fixes batch | Open PR #1429 |
| #1421 simulation-queue types | Open PR #1431; assignment requests 2026-10-13 |
| #1423 useState blocks | Open PR #1426; assignment request 2026-10-13 |
| #945 node deletion bug | Claim 2026-10-07 (within 60 days) |
| #469 setTimeout umbrella | Many claims, latest 2026-07-29; PR #1443 covers PropertiesPanel; umbrella, not a single fix |
| Interactive-Book #665 | Claim 2026-09-01 (inside window) |
| Interactive-Book #631 | Claim 2026-09-01; already fixed (#703 per comment) |
| mobile-app #84 | Claim and PR #651 on 2026-09-01 |
| CircuitVerseDocs #332 | Assignment requests 2026-08-11 and 2026-10-22 |
| cv-electron #5, #6 | No tests, vague, stale claim threads (not checked in depth) |
| CircuitVerse #7332, #7342 etc. (Rails) | Skipped per CTO (no ruby); #7332 has 14 comments, #7342 assigned |

## MetaBrainz (ENG-16) - INCOMPLETE, no fix made

**Status:** Stopped. No clone, no branch, no commit, nothing TESTED. Bash permission was denied partway through the issue search, so I cannot clone, run tests or commit. I did not try to work around it.

### Policy
Source: https://musicbrainz.org/doc/Development/Summer_of_Code/Getting_started and https://musicbrainz.org/doc/Development/Summer_of_Code/2026 (fetched 2026-10-31 via WebFetch; the 2026 page and Getting started page carry the same text).

- "We discourage the use of AI tools in communications and contributions."
- "The goal of GSoC is for you to learn and improve your skills, not just to finish your project at any cost."
- "However, if you do use any AI or LLMs, you must disclose their use in your PRs and/or conversations with your mentor."
- "Additionally, you must fully understand and be able to explain any AI-generated code you submit."
- "Any undisclosed use of AI or Large Language Models, or inability to explain AI-generated contributions, ... will be grounds for instant disqualification."
- Finding work: "Use the issue tracker to find something to work on, and use Git to submit patches." and "Looking for your first issue to work on? Try searching for issues labelled "Good First Bug" etc."

Repo CONTRIBUTING (https://github.com/metabrainz/musicbrainz-server/blob/master/CONTRIBUTING.md) has no AI text. It says: "Limit the subject line to 50 characters", "Wrap the body at 72 characters", "start the subject line with a ticket reference if applicable", PR titles prefixed "MBS-XXX:", and untracked changes (typos, comments, style) need no ticket.

**Verdict:** Not a ban, but materially limited. AI use is discouraged, must be disclosed in the PR, and the contributor must be able to explain every line. Undisclosed use means instant disqualification. The CEO should decide whether to proceed. If they do, the PR must carry the disclosure and Ankit must be able to explain the code unaided.

### Issue
None selected yet.

### Candidates checked (GitHub, read-only, `gh search issues --owner metabrainz --state open --label ...`)
| Label searched | Result |
|---|---|
| good first issue | 5 hits, all in metabrainz/listenbrainz-android (Kotlin, needs Android toolchain): #740, #694, #676, #596, #579. Not runnable here. Claim and PR checks not done. |
| good first bug | 0 |
| help wanted | 1: android #614, assigned to 07jasjeet. Rejected. |
| beginner / easy / newcomer | 0 each |

Not yet done: MetaBrainz's newcomer tickets live mostly in JIRA (tickets.metabrainz.org, label "Good First Bug" etc.). I had not yet looked there. Pure-Python repo candidates to inspect next: musicbrainzngs, brainzutils-python, mbdata, troi-recommendation-playground.

### Local path / Branch / Commit / Test command and output
None. UNTESTED, nothing built.

### Risks / open questions
- Bash denied mid-task, so the clone/test steps are blocked.
- AI policy risk above is real for the CEO's reputation with the org.
- Only Android issues carry the GitHub "good first issue" label; a Python fix will probably need a JIRA ticket.

## Learning Equality (Kolibri)

**Result: NO CLEAN ISSUE. No clone, no branch, no commit, no draft PR.** Checked 2026-10-31, read-only.

### Policy
Source: https://learningequality.org/contributing-to-our-open-code-base/ (read via WebFetch; the kolibri-dev.readthedocs.io contributing index and the org `.github` repo page have no AI or assignment text).

AI use is allowed, with conditions:
- "You're welcome to use generative AI to brainstorm solutions or generate code."
- "Pull requests and comments that appear to be written by AI," "giving off the impression that they have not been thoroughly understood, adjusted, and tested by the author" "won't be answered."
- "Share only relevant and actionable information that you verified"

Assignment process (this is what blocks us):
- "Find an unassigned 'help wanted' issue" and "request assignment in issue comments."
- "Focus solely on unassigned 'help wanted' issues."
- "Request up to two issue assignments at a time."
- "Do not open a pull request without being assigned the relevant issue."
- "If there are none free, wait until new ones are added."

Verdict: AI code is not banned, so the AI rule alone does not stop us. The process does: only unassigned "help wanted" issues are in scope, and a PR needs prior assignment (a comment only the CEO can post).

### Issue
None qualifies.

### Why it is free
Not applicable. Evidence that nothing is free:
- `gh search issues --owner learningequality --label "help wanted" --state open --limit 40` returned 21 issues. 20 have an assignee. The 21st is `test-actions#87` "Test 'help wanted' issue", a bot test fixture, not real work.
- `gh issue list --repo learningequality/le-utils --state open`: 13 issues, none labelled help wanted or newcomer. 5 are assigned to `rtibblesbot` (maintainer bot); the rest are old design or data questions (e.g. #181 migration to code generation, #159 jsonschema upgrade), unlabelled.
- `gh issue list --repo learningequality/ricecooker --label "help wanted"`: empty.
- `gh search issues --owner learningequality --label "good first issue" --state open`: 3 issues. Two assigned (kolibri#15408, #15390). One unassigned: `kolibri-docs#165`, see below.

kolibri-docs#165 "Unify community forum references and move to include file" (labels: enhancement, good first issue; no assignee; 1 comment dated 2025-01-11, not a claim; `gh pr list --repo learningequality/kolibri-docs --search "165" --state all` returned `[]`). I rejected it because:
1. It has no "help wanted" label, so under the org rule above it is not an issue they hand out.
2. It is open-ended docs restructuring (the reporter says "perhaps we can figure out a way"), so a maintainer decision is needed on the shape of the fix. That fails "small and self-contained".
3. Docs only (RST), with no tests to run.
4. Last activity is nearly 2 years old; maintainers may not want it.

### Local path / Branch / Commit
None. Nothing cloned.

### Test command and output
None. Nothing changed. Not UNTESTED, simply no code.

### Changed lines explained
None.

### Draft PR description
None.

### Risks / open questions
- A `gh api` call to list org `.github` files was denied by the session permission layer; I did not work around it and used WebFetch of the public repo page instead. Contributor text there only points to the page quoted above.
- "help wanted" supply is tiny and bot-and-volunteer heavy (20 of 21 assigned, many updated within the last week). New ones appear but get claimed fast. If the CEO wants Learning Equality, the practical path is to watch the `help wanted` label and request assignment immediately, then draft. Decision for CEO: wait and retry later, or drop this org for wave 2.
- If the CEO wants to pursue kolibri-docs#165 anyway, first ask in the issue whether maintainers want it and how (a `.. include::` snippet vs a substitution). That is a CEO action, not mine.
- Kolibri itself is heavy (Django, Jest); the unassigned items in le-utils are all unlabelled design work.

### Candidates checked
| Repo / issue | Label | Assignee | Verdict |
|---|---|---|---|
| kolibri#15703, 15670, 15666, 15662, 15639, 15597, 15594, 15569, 15568, 15552, 15550, 15536 | help wanted | yes (all) | assigned |
| kolibri#15408, 15390 | good first issue + help wanted | yes | assigned |
| studio#6346, 6140, 6139, 5933, 5932, 5931 | help wanted | yes (all) | assigned |
| kolibri-design-system#1385 | help wanted | yes | assigned |
| test-actions#87 | help wanted | none | bot test fixture |
| le-utils#253, 187, 186, 185, 184 | none / enhancement | rtibblesbot | assigned to bot |
| le-utils#181, 173, 159, 108, 73, 75, 67, 61, 30 | none (173: P2) | none | no newcomer label, design/data work |
| kolibri-docs#165 | good first issue | none | no help wanted label, vague docs scope, no tests |
| ricecooker help wanted | n/a | n/a | zero issues |
