---
status: approved
requested_by: coo
type: publish
task: MKT-3
requested: 2026-10-30
decided: 2026-10-30
---

## What is being asked
Standing approval for the office to ideate, make and publish The Early PM Instagram content (reels, carousels, stories) on its own via `/insta-cycle`, without per-post CEO approval.

## Why now
The CEO wants a self-running loop: post, measure, learn, post better.

## Cost / risk
- Cloudinary free tier and Scalekit; no paid spend approved here. Any paid tier still needs CEO approval.
- Risk: a wrong claim goes public. Mitigation: every VERIFY number is source-checked or cut; content rules in `.claude/commands/insta-cycle.md`.
- Hard caps in `tools/insta.py`: 2 feed posts and 5 stories per IST day. Kill switch: create `products/the-early-pm/PAUSE`.

## What happens if approved
`tools/insta-cycle.sh` runs `/insta-cycle` twice a day (launchd). Posts go out under the CEO's connected Instagram account.

## What happens if rejected
Packs stay in `products/the-early-pm/ready/` for manual posting.

## Evidence (links)
- `.claude/commands/insta-cycle.md`, `tools/insta.py`

CEO, 2026-10-30: "Agent will decide what to post, when to post everything. I won't interfere."
