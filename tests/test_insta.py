"""insta.py: Cloudinary signing, daily caps and the no-double-post guard."""
import json, os, sys, tempfile, unittest
from unittest import mock

sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "tools"))
import insta  # noqa: E402


class InstaTest(unittest.TestCase):
    def test_signature_matches_cloudinary_docs(self):
        # Example from cloudinary.com/documentation/authentication_signatures
        params = {"eager": "w_400,h_300,c_pad|w_260,h_200,c_crop", "public_id": "sample_image", "timestamp": "1315060510"}
        self.assertEqual(insta.cloudinary_signature(params, "abcd"), "bfd09f95f331f558cbd1320e67aa8d488770583e")

    def test_cap_counts_only_today_and_kind(self):
        with tempfile.TemporaryDirectory() as d:
            log = os.path.join(d, "log.jsonl")
            rows = [{"date": insta.today(), "kind": "feed"}, {"date": insta.today(), "kind": "story"},
                    {"date": "2000-01-01", "kind": "feed"}]
            open(log, "w").write("\n".join(json.dumps(r) for r in rows) + "\n")
            self.assertEqual(insta.posted_today("feed", log), 1)
            self.assertEqual(insta.posted_today("story", log), 1)

    def test_pause_and_already_posted_block_posting(self):
        with tempfile.TemporaryDirectory() as d:
            pause = os.path.join(d, "PAUSE")
            open(pause, "w").close()
            with mock.patch.object(insta, "PAUSE", pause), self.assertRaises(SystemExit):
                insta.guard("feed")
            open(os.path.join(d, "POSTED.json"), "w").write("{}")
            with mock.patch.object(insta, "PAUSE", pause + "-missing"), \
                 mock.patch.object(insta, "LOG", os.path.join(d, "none.jsonl")), self.assertRaises(SystemExit) as e:
                insta.post(d)
            self.assertIn("Already posted", str(e.exception))


if __name__ == "__main__":
    unittest.main()
