---
key: ENG-19
title: "GSoC wave 2: AOSSIE (other repos) first issue and tested local fix"
type: task
product: Company
status: In Review
category: In Review
priority: P2
owner: frontend-engineer-2
reporter: coo
created: 2026-10-31
due: 2026-11-07
links: [workspace/confluence/research/gsoc-wave2.md, workspace/confluence/research/gsoc-first-issues.md]
---

## Goal
Draft one small, tested fix for AOSSIE (other repos) that the CEO (Ankit Jha) reviews and submits as a PR under their own GitHub account.

## Acceptance criteria
- [ ] Contributor guide and AI policy read and quoted with URL. If AI-written code is banned or limited: no draft, reason stated.
- [ ] One issue: open, unassigned, newcomer label, no linked/open PR, no claim comment in last 60 days (comments read). Evidence recorded.
- [ ] Clone at /Users/ankitkumar/gsoc-oss/<repo> (depth 50), local branch gsoc/<issue>-<slug>, fix committed locally; verified with git log/status.
- [ ] Tests/lint run and passing in-session, real command and output pasted; else marked UNTESTED.
- [ ] QA by qa-functional (Divya).
- [ ] Section in gsoc-wave2.md with draft PR description (org template + AI disclosure); approval filed.

## Hard rules
Read-only GitHub. No comment, claim, reaction, fork, push, PR or post. No pip/npm install, system packages, Docker or Vagrant.

## Notes / log
- 2026-10-31 · coo (Ankit): CEO follow-up to ENG-9/10/11. Opened task, routed to CTO (Rahul).
- 2026-10-31 · cto (Rahul): Owner frontend-engineer-2 (Nikhil), QA qa-functional (Divya). Rahul: small JS/TS or Python repo whose tests need no install. NOT IndexedDB-Import-Export #114.
- 2026-10-31 · frontend-engineer-2 (Nikhil): Template-Repo #73 (dependabot groups). Free: no assignee, no open PR, last claim 2026-03-21. Branch gsoc/73-dependabot-groups, commit 17818ef, 41 lines added to .github/dependabot.yml. YAML parse passes (npx js-yaml); Dependabot itself cannot be tested locally.
- 2026-10-31 · coo (Ankit): Verified 17818ef with git log/status (clean tree). Sent to QA.
- 2026-10-31 · qa-functional (Divya): Accept with notes. Diff matches, 13 groups blocks, YAML exit 0, issue still free. The PR draft was missing the template's AI Notice section.
- 2026-10-31 · coo (Ankit): AI Notice restored. Approval filed: workspace/approvals/2026-10-31-aossie-template-repo-73-pr.md. Waiting for the CEO.
- 2026-11-03 · coo (Ankit): CEO asked in chat to fix the shortlisted issues and raise PRs. Issue still free on the day. Pushed the branch to the ankitjha1405 fork and opened https://github.com/AOSSIE-Org/Template-Repo/pull/172. The Discord claim has not been posted, and the CEO still needs to tick the PR checklist. Re-scanned AOSSIE, Zulip and Rocket.Chat for good first issues: none are free (Skills #8 claimed by its author, EduAid #592 has open PRs #596/#633, DebateAI #431 is covered by a maintainer PR).
- 2026-11-03 · coo (Ankit): Swept about 60 new AOSSIE issues created since 2026-09-15. Only DebateAI #797 (Play Online popup overflows on mobile, opened today, no claim, no PR) was free and small. Root cause: fixed w-[42rem] modal. Fix is on local branch fix/797-room-browser-mobile (commit 010de01) in ~/gsoc-oss/DebateAI. Checked at 375px with a static mock in headless Chrome: card 659px to 343px, Join button visible. PR not opened: npm ci was blocked in session, so the frontend tests have not run (AOSSIE requires local testing). PR draft is in the session scratchpad.
- 2026-11-03 · coo (Ankit): Third sweep, using a GraphQL search that sees PR cross-references. About 200 AOSSIE issues since 2026-05 and about 200 Rocket.Chat issues (core, ReactNative, Electron) since 2026-08. Every issue small enough to fix has an open PR or a claim comment, usually within a day. Most AOSSIE authors open the issue and the PR together. No new PR opened. Proposed to the CEO: a scheduled watcher for new issues, or new orgs.
