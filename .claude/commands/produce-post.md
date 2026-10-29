---
description: Turn one day of The Early PM content calendar into a ready-to-post folder (script, video or slides, caption)
argument-hint: <date YYYY-MM-DD, or "week YYYY-MM-DD" for Mon-Fri of that week>
---

Produce The Early PM post(s) for: $ARGUMENTS

As Ankit (COO), for each date:

1. Read the row in `workspace/confluence/products/the-early-pm/content-calendar.md`. Skip rows already Ready or Posted.
2. **Script.** If the date has no pack in `workspace/confluence/products/the-early-pm/week-*-posts.md`, delegate to `scriptwriter` (Varun Khanna) with the same pack format as week 1: hypothesis, hook + 2 Trial Reel alt hooks, timed script or slide copy, on-screen text, caption (1 ask, 3 hashtags), sources, VERIFY flags on any unconfirmed number. Use the `ig-reel`, `ig-carousel`, `ig-caption` and `ig-human` skills. Set status Scripted.
3. **Make it.** Output goes to `products/the-early-pm/ready/<date>/`.
   - Carousel: render 1080x1350 PNG slides with the `ig-carousel` skill as `slide-01.png`...
   - Reel: 1080x1920 MP4, 20-40 s, faceless. Voiceover with Kokoro `af_heart` (spell hard words phonetically). Pick the video skill by fit (CEO decision 2026-10-30):
     - `hyperframes` (faceless-explainer workflow): default for text-card and number reels.
     - `onetake`: reels built from real UI or screen recordings. Noncommercial license: stop and ask the CEO before using it once the page earns money.
     - `lemo-opuscar`: only for a story told in an art style.
   - Screen recordings the CEO must capture: do not fake them. Leave a placeholder clip, list the exact shots in `TODO.md`, and set status Scripted, not Ready.
   - Burn in captions. Keep text inside the 4:5 safe area so the grid crop works.
4. **Pack.** In the same folder write `caption.txt` (paste-ready), `alt-hooks.txt`, and `CHECKLIST.md`: every VERIFY item, the post time, and the cover frame.
5. Watch or view the output once before calling it done. Set the calendar row to Edited, then Ready when nothing is left in `TODO.md`. Log it in the MKT task.
6. Never post, schedule or upload anything. Report to the CEO: what is ready, what needs them (VERIFY checks, recordings), and the folder path.
