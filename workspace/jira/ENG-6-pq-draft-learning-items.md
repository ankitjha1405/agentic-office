---
key: ENG-6
title: "Product Quest: draft learning items reachable by slug (to-check 2)"
type: bug
product: Product Quest
status: In Review
category: In Review
priority: P2
owner: frontend-engineer-2
reporter: cto
created: 2026-10-29
due: 2026-10-30
links: [/Users/ankitkumar/dev/product-quest-fixes/replica/bugs.md]
---

## Goal
Confirm from the code whether a learning item with status != 'published' is reachable by slug. If yes, the item page treats it as not found.

## Acceptance criteria
- [ ] Finding recorded (code reading only; no writes to the shared production DB)
- [ ] If reachable: page returns not-found for non-published items; one commit; bugs.md updated
- [ ] tsc and eslint clean; e2e suite still passes

## Notes / log
- 2026-10-29 · coo (Ankit): CEO asked for the check. Routed to CTO.
- 2026-10-29 · cto (Rahul): Owner frontend-engineer-2 confirmed. Code reading: yes, reachable. page.tsx queries by slug only (l.20, l.40-43); canAccess() checks tier/stage, not status. Fix: add eq(learningItem.status,'published') in page.tsx (both queries) and opengraph-image.tsx:22; status is content visibility, filtered inline elsewhere, so invariant 2 holds. Same gap in lesson/[lessonId]/page.tsx and quiz.ts:67 (test route): include or file follow-up.
- 2026-10-29 · frontend-engineer-2 (Nikhil): added eq(learningItem.status,'published') via and() to both slug queries in learning/[slug]/page.tsx and the query in opengraph-image.tsx (import and); lesson/[lessonId] and quiz.ts untouched (follow-up); not run: tests/commit (shell blocked)
- 2026-10-29 · coo (Ankit): Reviewed diff: matches criteria. bugs.md updated. Lesson/quiz gap needs a CEO call: follow-up task or leave. Open: tests and commit (shell blocked).
