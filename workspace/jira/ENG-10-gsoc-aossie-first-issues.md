---
key: ENG-10
title: "GSoC 2027: AOSSIE first-issue shortlist and local draft fixes"
type: task
product: Company
status: In Review
category: In Review
priority: P2
owner: backend-engineer-2
reporter: coo
created: 2026-10-30
due: 2026-11-06
links: [workspace/confluence/research/gsoc-orgs-research.md, workspace/confluence/research/gsoc-first-issues.md, workspace/jira/PROD-1-gsoc-orgs-research.md]
---

## Goal
Prepare the CEO's first AOSSIE contribution for GSoC 2027. The CEO reviews, learns and submits every contribution under their own GitHub account.

## Acceptance criteria
- [ ] Contributor guide and AI/LLM-use policy read and quoted with URL. If AI-written code is banned or limited: no code drafted, learning guide written instead.
- [ ] Real good-first-issue label names verified on GitHub (AOSSIE-Org repos).
- [ ] 5 open, unassigned issues with no open linked PR and no recent claim comment, ranked for a Python/JS/TS beginner.
- [ ] Top 1-2 issues (if AI allowed): shallow clone at /Users/ankitkumar/dev/oss/<repo>, local branch gsoc/<issue>-<slug>, minimal fix committed locally, light tests/lint run or reason stated.
- [ ] QA review recorded.
- [ ] Section in workspace/confluence/research/gsoc-first-issues.md; claim/PR approval filed in workspace/approvals/.

## Hard rules
Read-only GitHub. No comments, claims, reactions, forks, pushes, PRs, chat posts, or writing gh commands. No system packages, Vagrant or Docker.

## Notes / log
- 2026-10-30 · coo (Ankit): CEO follow-up to PROD-1. Opened task, routed to CTO (Rahul) to assign an engineer and QA.
- 2026-10-30 · cto (Rahul): Owner backend-engineer-2 (Harpreet), QA qa-functional (Divya). Tip: skip Flutter repos; pick a Python/JS repo with working tests (pytest in venv or npm test); follow each repo README.
- 2026-10-30 · backend-engineer-2 (Harpreet): AI allowed with disclosure (https://github.com/AOSSIE-Org/Info/blob/main/Rules/AI.md). Labels "good first issue" (+ "help wanted" rare). Field crowded: most issues claimed or have PRs. Top pick IndexedDB-Import-Export #114 (unclaimed, no PR). Shallow clone at /Users/ankitkumar/dev/oss/IndexedDB-Import-Export. Branch/fix/tests not done: Bash denied.
- 2026-10-30 · coo (Ankit): git/npm need approval not available in this run, also in main session. No workaround. Harpreet drafts fix as uncommitted edits in the clone; CEO creates branch, runs tests, commits.
- 2026-10-30 · backend-engineer-2 (Harpreet): #114 fix drafted (uncommitted) in src/core/importer.ts: all records deserialized before openDatabaseForImport; insertRecords takes decoded records. Two vitest cases added (overwrite, merge with invalid date). PR body follows template with AI disclosure. Not run. Open: duplicate-key ConstraintError under overwrite left to maintainers. #421 and #768 show no linked PR.
- 2026-10-30 · coo (Ankit): Sent to qa-functional (Divya) for static review.
- 2026-10-30 · qa-functional (Divya): Accept with notes (static, nothing run). Fix covers overwrite and merge; tests would fail on old code. Overwrite can still lose data on write-time errors (duplicate keys, missing keyPath, bad out-of-line key, unique index). New behaviour: bad record in an orphan store now rejects import; PR body must say so. Added missing "AI Notice" template section. Prettier on test lines ~97 chars unverified.
- 2026-10-30 · coo (Ankit): QA notes applied to the PR body. Section written to workspace/confluence/research/gsoc-first-issues.md. Approval filed: workspace/approvals/2026-10-30-aossie-idb-114-claim-and-pr.md. Waiting for CEO: approval, then CEO runs branch/tests/commit.
