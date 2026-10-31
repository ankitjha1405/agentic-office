---
key: ENG-18
title: "GSoC wave 2: Django first issue and tested local fix"
type: task
product: Company
status: Blocked
category: Blocked
priority: P2
owner: backend-engineer-1
reporter: coo
created: 2026-10-31
due: 2026-11-07
links: [workspace/confluence/research/gsoc-wave2.md, workspace/confluence/research/gsoc-first-issues.md]
---

## Goal
Draft one small, tested fix for Django that the CEO (Ankit Jha) reviews and submits as a PR under their own GitHub account.

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
- 2026-10-31 · cto (Rahul): Owner backend-engineer-1 (Aditya), QA qa-functional (Divya). Rahul: asgiref+sqlparse on PYTHONPATH, tests/runtests.py <module> on SQLite. Trac easy-pickings tickets.
- 2026-10-31 · backend-engineer-1 (Aditya): AI allowed with disclosure; no AI reviews on PRs (quoted from submitting-patches.txt). Trac list pages return 403 to WebFetch; 12 single tickets checked, none free. Clean clone of main at /Users/ankitkumar/gsoc-oss/django, no branch.
- 2026-10-31 · coo (Ankit): My curl of the Trac CSV export was denied; not worked around. Blocked on CEO: send 2-3 easy-pickings ticket numbers from a browser, or drop Django.
