---
key: ENG-9
title: "GSoC 2027: Zulip first-issue shortlist and local draft fixes"
type: task
product: Company
status: In Review
category: In Review
priority: P2
owner: backend-engineer-1
reporter: coo
created: 2026-10-30
due: 2026-11-06
links: [workspace/confluence/research/gsoc-orgs-research.md, workspace/confluence/research/gsoc-first-issues.md, workspace/jira/PROD-1-gsoc-orgs-research.md]
---

## Goal
Prepare the CEO's first Zulip contribution for GSoC 2027. The CEO reviews, learns and submits every contribution under their own GitHub account.

## Acceptance criteria
- [ ] Contributor guide and AI/LLM-use policy read and quoted with URL. If AI-written code is banned or limited: no code drafted, learning guide written instead.
- [ ] Real good-first-issue label names verified on GitHub (zulip/zulip).
- [ ] 5 open, unassigned issues with no open linked PR and no recent claim comment, ranked for a Python/JS/TS beginner.
- [ ] Top 1-2 issues (if AI allowed): shallow clone at /Users/ankitkumar/dev/oss/<repo>, local branch gsoc/<issue>-<slug>, minimal fix committed locally, light tests/lint run or reason stated.
- [ ] QA review recorded.
- [ ] Section in workspace/confluence/research/gsoc-first-issues.md; claim/PR approval filed in workspace/approvals/.

## Hard rules
Read-only GitHub. No comments, claims, reactions, forks, pushes, PRs, chat posts, or writing gh commands. No system packages, Vagrant or Docker.

## Notes / log
- 2026-10-30 · coo (Ankit): CEO follow-up to PROD-1. Opened task, routed to CTO (Rahul) to assign an engineer and QA.
- 2026-10-30 · cto (Rahul): Owner backend-engineer-1 (Aditya), QA qa-automation (Manish). Tip: prefer a web/ issue; run one web/tests/*.test.cjs with node; ruff/mypy on changed Python only (backend suite needs provisioned env).
- 2026-10-30 · backend-engineer-1 (Aditya): AI policy read (https://zulip.readthedocs.io/en/latest/contributing/contributing.html#ai-use-policy-and-guidelines): AI allowed only if the contributor understands and tests every line; do not use an LLM to find things to work on; no AI-written messages. Bash denied in agent session, shortlist not done.
- 2026-10-30 · coo (Ankit): Policy limits AI code, so per CEO rule Zulip gets a learning guide, no drafted code. Verified newcomer label is "help wanted" (0 open "good first issue"). Sent Aditya back to finish the shortlist via read-only GitHub API.
- 2026-10-30 · backend-engineer-1 (Aditya): Checked 12 "help wanted" issues; 10 dropped for open PRs or recent claims (incl. #40026: PRs #40027, #40032). Survivors: #17428 (sort API response keys, Python) and #5090 (deactivated_redirect in server_settings, Python; PR #39093 closed unmerged 2026-09-02). Learning guides for both written. PR search hit API 403 partway: CEO must recheck PRs before claiming.
- 2026-10-30 · qa-automation (Manish): Both survivors fail: #17428 has open PR #38826, #5090 has open PR #40231. 0 of 12 viable. Guide paths corrected; added missing policy rules and PR template heading.
- 2026-10-30 · coo (Ankit): Section written to workspace/confluence/research/gsoc-first-issues.md. Learning guides kept as study material. No approval filed: no claimable issue. Next: CEO picks a "help wanted" issue personally (fits Zulip's policy) and reruns the two checks.
