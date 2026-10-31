---
key: ENG-16
title: "GSoC wave 2: MetaBrainz first issue and tested local fix"
type: task
product: Company
status: Done
category: Complete
priority: P2
owner: backend-engineer-2
reporter: coo
created: 2026-10-31
due: 2026-11-07
links: [workspace/confluence/research/gsoc-wave2.md, workspace/confluence/research/gsoc-first-issues.md]
---

## Goal
Draft one small, tested fix for MetaBrainz that the CEO (Ankit Jha) reviews and submits as a PR under their own GitHub account.

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
- 2026-10-31 · cto (Rahul): Owner backend-engineer-2 (Harpreet), QA qa-functional (Divya). Rahul: Picard needs PyQt, ListenBrainz Docker, MB server Perl. Pick small pure-Python lib repo.
- 2026-10-31 · backend-engineer-2 (Harpreet): The musicbrainz.org GSoC page says "We discourage the use of AI tools in communications and contributions"; undisclosed AI use means disqualification. The only GitHub good-first-issues are Android/Kotlin. JIRA not searched (Bash denied mid-task).
- 2026-10-31 · coo (Ankit): AI-limited per the CEO rule. Skipped, no draft. Section in gsoc-wave2.md.
