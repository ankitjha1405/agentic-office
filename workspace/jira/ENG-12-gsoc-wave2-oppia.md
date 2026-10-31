---
key: ENG-12
title: "GSoC wave 2: Oppia first issue and tested local fix"
type: task
product: Company
status: Done
category: Complete
priority: P2
owner: frontend-engineer-1
reporter: coo
created: 2026-10-31
due: 2026-11-07
links: [workspace/confluence/research/gsoc-wave2.md, workspace/confluence/research/gsoc-first-issues.md]
---

## Goal
Draft one small, tested fix for Oppia that the CEO (Ankit Jha) reviews and submits as a PR under their own GitHub account.

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
- 2026-10-31 · cto (Rahul): Owner frontend-engineer-1 (Sneha), QA qa-functional (Divya). Rahul: tests need GAE+Karma; only a pure TS helper under npx vitest has a chance. Time-boxed; else docs-only UNTESTED or skip.
- 2026-10-31 · frontend-engineer-1 (Sneha): No clean issue. All 17 open good-first-issues were claimed or assigned by comment between 2026-10-13 and 10-28, or need GAE/Karma/Playwright to test. No AI policy found (wiki not fully searched). Oppia requires assignment via comment first. No clone or draft.
- 2026-10-31 · coo (Ankit): Closed for this wave with no fix. Section in gsoc-wave2.md. To unlock: the CEO asks for assignment in their own words.
