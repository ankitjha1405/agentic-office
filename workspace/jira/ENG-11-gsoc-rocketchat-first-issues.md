---
key: ENG-11
title: "GSoC 2027: Rocket.Chat first-issue shortlist and local draft fixes"
type: task
product: Company
status: In Review
category: In Review
priority: P2
owner: frontend-engineer-1
reporter: coo
created: 2026-10-30
due: 2026-11-06
links: [workspace/confluence/research/gsoc-orgs-research.md, workspace/confluence/research/gsoc-first-issues.md, workspace/jira/PROD-1-gsoc-orgs-research.md]
---

## Goal
Prepare the CEO's first Rocket.Chat contribution for GSoC 2027. The CEO reviews, learns and submits every contribution under their own GitHub account.

## Acceptance criteria
- [ ] Contributor guide and AI/LLM-use policy read and quoted with URL. If AI-written code is banned or limited: no code drafted, learning guide written instead.
- [ ] Real good-first-issue label names verified on GitHub (RocketChat/Rocket.Chat and related repos).
- [ ] 5 open, unassigned issues with no open linked PR and no recent claim comment, ranked for a Python/JS/TS beginner.
- [ ] Top 1-2 issues (if AI allowed): shallow clone at /Users/ankitkumar/dev/oss/<repo>, local branch gsoc/<issue>-<slug>, minimal fix committed locally, light tests/lint run or reason stated.
- [ ] QA review recorded.
- [ ] Section in workspace/confluence/research/gsoc-first-issues.md; claim/PR approval filed in workspace/approvals/.

## Hard rules
Read-only GitHub. No comments, claims, reactions, forks, pushes, PRs, chat posts, or writing gh commands. No system packages, Vagrant or Docker.

## Notes / log
- 2026-10-30 · coo (Ankit): CEO follow-up to PROD-1. Opened task, routed to CTO (Rahul) to assign an engineer and QA.
- 2026-10-30 · cto (Rahul): Owner frontend-engineer-1 (Sneha), QA qa-automation (Manish). Tip: pick an issue inside one packages/* workspace; run only its jest + eslint on changed files; skip Meteor app and E2E.
- 2026-10-30 · frontend-engineer-1 (Sneha): GSoC 2026 page bans LLM-written proposals, allows AI for research; no code-AI rule found in CONTRIBUTING. "good first issue" label confirmed. Bash denied in agent session, nothing cloned.
- 2026-10-30 · coo (Ankit): AI code allowed, drafting in scope. Sneha finishes claim/PR checks via read-only GitHub API and specs the fix; Ankit clones, tests and commits from the main session.
- 2026-10-30 · frontend-engineer-1 (Sneha): No clean issue found. Rocket.Chat #26723 has ~20 open PRs; EmbeddedChat #1276/#1315/#1284/#1313/#1373/#1287/#1286/#1317/#1377/#1372 all claimed or have PRs; Livechat archived; Apps.Notion dormant. Remaining monorepo issues unchecked: GitHub API quota hit (403).
- 2026-10-30 · coo (Ankit): git/npm need approval not available in this run (main session too); no workaround. One retry of the search after the API quota resets.
- 2026-10-30 · coo (Ankit): Retry skipped: remaining candidates are in the Meteor monorepo (not cheaply testable). Section written to workspace/confluence/research/gsoc-first-issues.md. No approval filed: no claimable issue. Next: check unlabelled EmbeddedChat issues (e.g. #1294) by hand, then send the number to Sneha for a draft.
