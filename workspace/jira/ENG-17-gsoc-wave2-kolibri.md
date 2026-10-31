---
key: ENG-17
title: "GSoC wave 2: Learning Equality (Kolibri) first issue and tested local fix"
type: task
product: Company
status: Done
category: Complete
priority: P2
owner: backend-engineer-1
reporter: coo
created: 2026-10-31
due: 2026-11-07
links: [workspace/confluence/research/gsoc-wave2.md, workspace/confluence/research/gsoc-first-issues.md]
---

## Goal
Draft one small, tested fix for Learning Equality (Kolibri) that the CEO (Ankit Jha) reviews and submits as a PR under their own GitHub account.

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
- 2026-10-31 · cto (Rahul): Owner backend-engineer-1 (Aditya), QA qa-functional (Divya). Rahul: full app too heavy; prefer le-utils or another small pure-Python repo.
- 2026-10-31 · backend-engineer-1 (Aditya): AI allowed ("welcome to use generative AI"), but no PR without assignment. 20 of 21 open help-wanted issues org-wide are assigned; the 21st is a bot fixture. kolibri-docs#165 rejected (no help-wanted label, needs a maintainer decision). No clone or draft.
- 2026-10-31 · coo (Ankit): Closed for this wave with no fix.
