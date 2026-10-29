---
key: ENG-8
title: "Haunted Terminal: music lock file opened without closing (ResourceWarning)"
type: bug
product: Haunted Terminal
status: In Review
category: In Review
priority: P3
owner: backend-engineer-2
reporter: cto
created: 2026-10-29
due: 2026-10-30
links: [/Users/ankitkumar/haunted-terminal/replica/bugs.md]
---

## Goal
`ghost` (~line 471) opens the music lock file with a with-block so it is closed.

## Acceptance criteria
- [ ] `python3 -m unittest -v test_ghost.py` passes with no ResourceWarning
- [ ] One commit; bugs.md updated
- [ ] BUG-004 (private repo) left open: CEO decision, repo visibility not changed

## Notes / log
- 2026-10-29 · coo (Ankit): CEO asked for the fix. Routed to CTO.
- 2026-10-29 · cto (Rahul): Owner backend-engineer-2 confirmed. File: /Users/ankitkumar/haunted-terminal/ghost:472, wrap open(lock).read() in a with-block. Same function: fd leaks if os.write (l.467) raises; optional try/finally.
- 2026-10-29 · backend-engineer-2 (Harpreet): ghost: lock read now in with-block; fd closed via try/finally if os.write raises; not run: tests/commit (shell blocked)
- 2026-10-29 · coo (Ankit): Reviewed diff: matches criteria. bugs.md updated; BUG-004 left open for CEO. Open: unittest and commit (shell blocked).
