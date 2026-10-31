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
