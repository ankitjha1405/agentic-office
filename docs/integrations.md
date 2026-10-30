# Jira and Confluence integration

Both integrations are optional. The office works entirely from local files in `workspace/`. When you add credentials, hooks in `.claude/settings.json` mirror those files after every change:

- **Tasks** in `workspace/jira/` become Jira issues.
- **Documents** in `workspace/confluence/` (plus `CLAUDE.md` and `ROSTER.md`) become Confluence pages.

The files stay the source of truth. Edits made directly in Jira or Confluence are overwritten by the next file change, except Jira comments, which come back into the task files via `/pull-comments`.

## What you need

- An Atlassian Cloud site (`https://your-team.atlassian.net`). The Free plans of Jira and Confluence work (up to 10 users; every agent publishes through your one login, so they count as one user).
- An Atlassian API token: [id.atlassian.com → Security → API tokens](https://id.atlassian.com/manage-profile/security/api-tokens).
- Python 3.9 or newer. No packages to install.

## 1. Fill in `.env`

```bash
cp .env.example .env
```

```ini
JIRA_SITE=https://your-team.atlassian.net
JIRA_EMAIL=you@example.com
JIRA_API_TOKEN=your-token
JIRA_PROJECT_KEY=AGENTIC
CONFLUENCE_SPACE_KEY=AO
CONFLUENCE_SPACE_NAME=Agentic Office
```

`.env` is in `.gitignore`, and `.claude/settings.json` stops agents from reading it. Never commit it.

## 2. Jira

1. **Create a project** in Jira: Projects → Create project → **Kanban** → company-managed. Use the key you put in `JIRA_PROJECT_KEY`.
2. **Check the connection:**
   ```bash
   python3 tools/jira_sync.py check
   ```
   It prints your name, the project, its issue types and statuses.
3. **Add the office's stages** (Blocked and In Review) to the workflow and the board:
   ```bash
   python3 tools/jira_sync.py setup
   ```
   Your board becomes: Backlog → Selected for Development → In Progress → Blocked → In Review → Done. If your project type doesn't allow this through the API, the command tells you how to add the two columns by hand.
4. **Push existing tasks:**
   ```bash
   python3 tools/jira_sync.py sync
   ```

### How tasks map to Jira

| Task file | Jira |
|---|---|
| `key: ENG-4`, `title` | Summary `[ENG-4] <title>`, labels `office` and `office-ENG-4` |
| Key prefix (`ENG`, `PROD`, …) | Department label (`engineering`, `product`, …) |
| `priority: P1` | Label `P1` |
| `type: bug / story / epic / task` | Issue type (falls back to Task if the project doesn't have it) |
| `category: Not Started / Active / Blocked / In Review / Complete` | Backlog (or Selected for Development when the department status is Ready, Prioritized and similar) / In Progress / Blocked / In Review / Done |
| Owner, reporter, goal, acceptance criteria, due date | Issue description |
| Each line of `## Notes / log` | One issue comment, prefixed `[office]` |

**Comments from people:** anything you write on an issue without the `[office]` prefix is pulled into the task log by `/pull-comments` (also run by `/standup`). Ankit then answers or acts on it.

## 3. Confluence

1. **Add Confluence to your site** if it isn't there: [admin.atlassian.com](https://admin.atlassian.com) → your site → Products → Add product → Confluence (Free).
2. **Publish:**
   ```bash
   python3 tools/confluence_sync.py sync
   ```
   The first run creates the space (`CONFLUENCE_SPACE_KEY`) with an index home page, then one Confluence folder per folder in `workspace/confluence/` and one page per document.

### What each page gets

- **An owner panel** at the top: owner (the agent who wrote it, with full name), department, status, created, last updated, contributors and source file. All of it comes from the document's header; see [the documentation standard](../workspace/confluence/company/documentation-standard.md).
- **Labels:** `office`, `owner-<agent-name>`, and the department. Click a label to see everything one agent owns.
- **Working links:** links to other docs become Confluence page links, and links to task files become links to their Jira issues.

Page titles must be unique within a space; the documentation standard has agents prefix product docs with the product name.

## How the hooks work

`.claude/settings.json` runs both scripts with the `hook` command after every `Write`, `Edit` or `Bash` tool call, and when a session stops:

- They do nothing until their settings exist in `.env`.
- They only send what changed. Each script keeps a small state file (`.jira-state.json`, `.confluence-state.json`) that maps local files to Jira issues and Confluence pages. These files are git-ignored because they are specific to your site. Keep them: if you delete them, the next sync creates duplicates.
- They never block the agents. Errors go to `workspace/jira/.jira-sync.log` and `workspace/confluence/.confluence-sync.log`, and Ankit mentions them if they are not empty.

## Windows

The steps above are written for macOS and Linux. On Windows (PowerShell), change these:

| Step | macOS / Linux | Windows |
|---|---|---|
| Python command | `python3` | `py` (the python.org installer adds `py` and `python`, not `python3`) |
| Create `.env` | `cp .env.example .env` | `Copy-Item .env.example .env` |
| Run a script | `python3 tools/jira_sync.py check` | `py tools\jira_sync.py check` |
| Dry run | `JIRA_DRY_RUN=1 python3 tools/jira_sync.py sync` | `$env:JIRA_DRY_RUN=1; py tools\jira_sync.py sync` |

**The hooks.** Claude Code on Windows runs hook commands through Git Bash, so the quoted `"$CLAUDE_PROJECT_DIR/..."` paths in `.claude/settings.json` work as written, including paths with spaces. The hooks call `python3`, so check that `python3 --version` prints a version in Git Bash. If it doesn't (or it opens the Microsoft Store), either install Python from the Microsoft Store, which provides `python3`, or change `python3` to `py` in the four hook commands in your copy of `.claude/settings.json`.

**Encoding.** The scripts read and write files as UTF-8 on every platform, so names like "Zoë" and characters like "→" in task files survive the Windows default code page. A `.env` saved by Notepad with a byte-order mark also works.

## Troubleshooting

| Problem | Fix |
|---|---|
| `CERTIFICATE_VERIFY_FAILED` | Python from python.org on macOS lacks CA certificates. The scripts fall back to `certifi` or `/etc/ssl/cert.pem`. If both are missing, run "Install Certificates.command" in your Python folder. |
| `401` from Confluence | Confluence is not on your site yet, or the token belongs to a different account than `JIRA_EMAIL`. |
| `No project could be found with key` | Create the Jira project first, or fix `JIRA_PROJECT_KEY`. |
| Issue stays in In Progress instead of In Review | Run `python3 tools/jira_sync.py setup`, or add the column by hand. |
| Duplicate issues or pages | A state file was deleted. Delete the duplicates in Jira or Confluence; the state file is rebuilt as the sync runs. |
| Want to see what would be sent | Prefix a command with `JIRA_DRY_RUN=1` or `CONFLUENCE_DRY_RUN=1`. |

## Instagram (The Early PM)

`/insta-cycle` posts reels, carousels and stories on its own, pulls Insights, and rewrites `insta-learnings.md`. It runs at 10:00 and 17:30 via `~/Library/LaunchAgents/club.foxo.insta-cycle.plist`. Your Mac must be awake. Output goes to `workspace/insta-cycle.log`. To stop all posting, create `products/the-early-pm/PAUSE`.

One-time setup:

1. Make the Instagram account a Business or Creator account and link it to a Facebook Page.
2. Meta: create a Business-type app at developers.facebook.com. Add the Instagram Graph API and Facebook Login products.
3. Scalekit: sign up at app.scalekit.com. Go to AgentKit > Connections and create an Instagram connection. Choose "Use your own credentials", and enter the Meta app's App ID and App secret. Copy the redirect URI into Facebook Login > Settings > Valid OAuth Redirect URIs.
4. Cloudinary: sign up for the free tier. Copy the cloud name, API key and API secret.
5. Stories token: in Graph API Explorer, generate a user token with `instagram_basic`, `instagram_content_publish` and `pages_show_list`. Exchange it for a long-lived token (60 days). Read `IG_USER_ID` from `me/accounts?fields=instagram_business_account`.
6. Fill in the Instagram block of `.env` (see `.env.example`).
7. Install the SDK and sign in once:
   ```bash
   python3 -m venv .venv-insta && .venv-insta/bin/pip install scalekit-sdk-python
   .venv-insta/bin/python tools/insta.py auth      # open the printed link, sign in to Instagram
   .venv-insta/bin/python tools/insta.py insights  # should save a JSON file of recent posts
   ```
The stories token expires after 60 days. Renew it before then, or story posts will fail.
