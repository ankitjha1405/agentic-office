---
key: ENG-20
title: "OSS contributions outside GSoC orgs: Claude skills and other open-source projects"
type: task
product: Company
status: In Review
category: In Review
priority: P2
owner: coo
reporter: coo
created: 2026-11-03
due: 2026-11-17
links: [workspace/jira/ENG-19-gsoc-wave2-aossie.md]
---

## Goal
CEO asked (2026-11-03) to stop limiting the search to GSoC orgs and to fix issues in good skills or other open-source projects, then open PRs under the CEO's personal GitHub account.

## Acceptance criteria
- [x] Pick projects that merge outside PRs and whose fixes can be checked without installing their dependencies.
- [x] Each issue verified free (no linked or cross-referenced PR, no claim) before work.
- [x] PR body says how it was tested, what was not run, and discloses AI help.
- [ ] PRs merged or closed; follow up on review comments.

## Notes / log
- 2026-11-03 · coo (Ankit): Skipped anthropics/skills (only staff PRs are merged; 1,466 open issues). Skipped obra/superpowers issues (design proposals, not bugs).
- 2026-11-03 · coo (Ankit): SawyerHood/dev-browser #142. SKILL.md and README document the 1.0 API, but npm `latest` is still 0.2.9 (1.0 is on `next`). Install lines changed to `dev-browser@next`, plus a README note. Static assertions from docs.test.ts checked. PR https://github.com/SawyerHood/dev-browser/pull/147.
- 2026-11-03 · coo (Ankit): OthmanAdi/planning-with-files #359 (good first issue). The 5 localized /plan commands were translated to the resolver/init contract from #351, with a new language-neutral test and a CHANGELOG entry. The new checks fail on the old files and pass on the new ones, run from my own script: running the repo's test file and pytest was blocked in this session. PR https://github.com/OthmanAdi/planning-with-files/pull/364. Found, not fixed: the zh/zht/ar/es skills tell agents to write localized phase/status markers that check-complete.sh rejects.
- 2026-11-03 · coo (Ankit): Limits this session: npm ci, pytest and running external repos' test files are blocked by the permission classifier, so only changes that can be checked statically are picked.
