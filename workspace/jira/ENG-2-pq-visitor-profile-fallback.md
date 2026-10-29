---
key: ENG-2
title: "Product Quest: visitor /profile shows empty h1 and avatar (BUG-004)"
type: bug
product: Product Quest
status: In Review
category: In Review
priority: P2
owner: frontend-engineer-1
reporter: cto
created: 2026-10-29
due: 2026-10-30
links: [/Users/ankitkumar/dev/product-quest-fixes/replica/bugs.md]
---

## Goal
A visitor on /profile sees a sensible placeholder name and avatar initials, not blanks.

## Acceptance criteria
- [ ] h1 and avatar have a fallback when there is no profile name
- [ ] e2e `F10-E1 /profile headings all have text` passes
- [ ] tsc and eslint clean; one commit; bugs.md updated

## Notes / log
- 2026-10-29 · coo (Ankit): CEO asked for the fix. Routed to CTO.
- 2026-10-29 · cto (Rahul): Owner frontend-engineer-1 confirmed. File: src/app/(app)/profile/page.tsx (~l.89 h1 + avatar initials), fallback "Your profile". Same file as ENG-4, same owner, sequence them.
- 2026-10-29 · frontend-engineer-1 (Sneha): profile/page.tsx h1 falls back to "Your profile", avatar initials to "?" (null-safe fullName); not run: tests/commit (shell blocked)
- 2026-10-29 · coo (Ankit): Reviewed diff: matches criteria. bugs.md updated. Open: tests and commit (shell blocked); waiting on CEO.
