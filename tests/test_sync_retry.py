"""A call that fails after the create must not make the next run create a duplicate (issue #10)."""
import json, os, sys, tempfile, unittest
from unittest import mock

sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "tools"))
import confluence_sync, jira_sync  # noqa: E402

TASK = """---
key: ENG-1
title: Retry
owner: cto
status: in progress
category: In Progress
---
## Goal
Ship it.

## Notes / log
- 2026-10-30 · cto: one
- 2026-10-30 · cto: two
"""


class FakeApi:
    """Records calls; raises once, on the `nth` call whose path contains `fail`."""
    def __init__(self, fail, nth=1):
        self.fail, self.nth, self.calls = fail, nth, []

    def __call__(self, method, path, body=None, **kw):
        self.calls.append((method, path, body))
        if self.fail and self.fail in path:
            self.nth -= 1
            if not self.nth:
                self.fail = None
                raise RuntimeError("429 Too Many Requests")
        return {"key": "AO-1", "id": "1", "transitions": [], "comments": []}


class SyncRetryTest(unittest.TestCase):
    def setUp(self):
        self.dir = tempfile.mkdtemp()
        self.path = os.path.join(self.dir, "ENG-1-retry.md")
        with open(self.path, "w", encoding="utf-8") as fh:
            fh.write(TASK)

    def run_twice(self, module, fail, sync, env=None, nth=1):
        empty = json.dumps({"issues": {}, "pages": {}, "space": {"id": "S", "home": "H"}})
        disk = [empty]  # what .jira-state.json / .confluence-state.json holds; each hook run reloads it
        api = FakeApi(fail, nth)
        with mock.patch.object(module, "call", api), mock.patch.dict(os.environ, env or {}), \
                mock.patch.object(module, "save_state", lambda s: disk.__setitem__(0, json.dumps(s))):
            with self.assertRaises(RuntimeError):
                sync(json.loads(disk[0]))
            sync(json.loads(disk[0]))
        return [c for c in api.calls if c[0] == "POST"]

    def test_jira_no_duplicate_issue_or_comments(self):
        sync = lambda s: jira_sync.sync_file(self.path, s, {})
        # comments: "created", log "one", log "two" (fails on the first run)
        posts = self.run_twice(jira_sync, "/comment", sync, {"JIRA_PROJECT_KEY": "AO"}, nth=3)
        self.assertEqual([p for _, p, _ in posts].count("/issue"), 1)
        comments = [b for _, p, b in posts if p.endswith("/comment")]
        self.assertEqual(len(comments), len({str(b) for b in comments}) + 1)  # only the failed one is resent

    def test_confluence_no_duplicate_page(self):
        sync = lambda s: confluence_sync.sync_doc(self.path, None, {}, s, {})
        with mock.patch.object(confluence_sync, "ROOT", self.dir):
            posts = self.run_twice(confluence_sync, "/label", sync)
        paths = [p for _, p, _ in posts]
        self.assertEqual(paths.count("/api/v2/pages"), 1)
        self.assertEqual(paths.count("/rest/api/content/1/label"), 2)  # label call retried


if __name__ == "__main__":
    unittest.main()
