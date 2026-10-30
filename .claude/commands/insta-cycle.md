---
description: One autonomous Instagram round for The Early PM - measure, learn, decide, make, post (reels, carousels, stories)
argument-hint: (none; runs on a schedule via tools/insta-cycle.sh)
---

Run one Instagram cycle for The Early PM. The CEO gave standing approval to post on their own (`workspace/approvals/2026-10-30-standing-instagram-autopost.md`). Do not stop to ask the CEO anything. Run as Ankit (COO). Use `.venv-insta/bin/python tools/insta.py` for every Instagram call. Its daily caps and the `products/the-early-pm/PAUSE` file are hard limits: if it refuses, do not work around it.

1. **Stop check.** If `products/the-early-pm/PAUSE` exists, write one line in the MKT task log and end.
2. **Measure.** Run `insta.py insights`. Delegate to `growth-analytics` (Aishwarya): compare the new `products/the-early-pm/insights/<today>.json` with older pulls. Use the metrics in `workspace/confluence/products/the-early-pm/experiment-tracker.md`. Fill in tracker rows for posts 7+ days old. Rewrite `workspace/confluence/products/the-early-pm/insta-learnings.md`: what works (hook type, format, pillar, length, post time), what to stop, and one next experiment. Every claim needs its numbers and a confidence level.
3. **Decide.** Read `insta-learnings.md`, `content-calendar.md` and `products/the-early-pm/insta-log.jsonl`. Pick what to post today, in which format, and when (post now, or leave it for the next run). Re-plan calendar rows from the learnings when the evidence says so. Delegate idea work to `content-strategist` (Shreya), and use the `ig-plan` and `ig-viral` skills when the calendar runs dry. Target: 1 feed post (reel or carousel) and 1-3 stories a day.
4. **Make.** Use `/produce-post <date>` steps 1-5 for the feed post. Rules that replace CEO review:
   - Every VERIFY item gets checked against its source with WebFetch. If it does not match, or the source does not load, cut the claim. Never post an unchecked number.
   - A post needing a CEO screen recording is skipped, not faked. Pick another topic.
   - Run the `ig-human` skill on the caption.
   - Watch or view the output before posting.
   - Stories: write them with the `ig-story` skill and render each as a 1080x1920 PNG (or MP4 under 60 s) in `products/the-early-pm/ready/<date>/stories/`. Insights recaps, polls as plain text, behind-the-scenes from the build, and teasers for today's reel all work. Stickers cannot be added by API. Write story text so it needs none.
5. **Post.** Run `insta.py post products/the-early-pm/ready/<date>` and `insta.py story <file>` for each story. Set the calendar row to Posted. If a post fails, log the error and do not retry more than once.
6. **Record.** Append a one-line entry to the MKT task log: what was posted (media id), what was learned, and what is next. Add one line to `workspace/memory/growth-analytics.md` when a lesson changed.

Never post anything that names or shows a real person without their consent, anything medical, legal or financial advice, or claims about competitors that are not sourced. Before posting, check this list. If a post fails a check, drop it and post something else.
