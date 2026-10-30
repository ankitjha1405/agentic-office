#!/bin/bash
# Runs one /insta-cycle headless. Started twice a day by ~/Library/LaunchAgents/club.foxo.insta-cycle.plist.
cd "$(dirname "$0")/.." || exit 1
export PATH="$HOME/.local/bin:/opt/homebrew/bin:/usr/local/bin:$PATH"
grep -q '^IG_USER_ID=..*' .env || { echo "$(date) IG_USER_ID not set in .env, skipping" >> workspace/insta-cycle.log; exit 0; }
{ echo "=== $(date)"; claude -p "/insta-cycle" --permission-mode acceptEdits \
    --allowedTools "Bash Read Write Edit Glob Grep WebFetch WebSearch Agent Skill"; } >> workspace/insta-cycle.log 2>&1
