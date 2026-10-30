"""Instagram for The Early PM: post reels/carousels (Scalekit), stories (Meta Graph API), pull insights.

Usage (run with .venv-insta/bin/python, which has scalekit-sdk-python):
  insta.py auth                 print the one-time Instagram sign-in link
  insta.py post <ready-dir>     publish video.mp4 as a reel, or slide-*.png as a carousel, with caption.txt
  insta.py story <file>         publish one image or video as a story
  insta.py insights [N]         save reach/views/saves/shares for the last N posts (default 25)

Keys come from .env (see .env.example). Every post is appended to products/the-early-pm/insta-log.jsonl.
"""
import base64, datetime, glob, hashlib, json, os, sys, time, urllib.parse, urllib.request

from common import ROOT, SSL, load_env

PRODUCT = os.path.join(ROOT, "products", "the-early-pm")
LOG = os.path.join(PRODUCT, "insta-log.jsonl")
PAUSE = os.path.join(PRODUCT, "PAUSE")  # create this file to stop all posting
CAPS = {"feed": 2, "story": 5}  # per IST day; Instagram's own limit is 25 feed posts per 24 h
GRAPH = "https://graph.facebook.com/v21.0"
IST = datetime.timezone(datetime.timedelta(hours=5, minutes=30))


def today():
    return datetime.datetime.now(IST).date().isoformat()


def posted_today(kind, log=LOG):
    if not os.path.exists(log):
        return 0
    rows = [json.loads(l) for l in open(log, encoding="utf-8") if l.strip()]
    return sum(r["kind"] == kind and r["date"] == today() for r in rows)


def guard(kind):
    if os.path.exists(PAUSE):
        sys.exit(f"PAUSE file present ({PAUSE}): not posting.")
    if posted_today(kind) >= CAPS[kind]:
        sys.exit(f"Daily cap reached: {CAPS[kind]} {kind} posts today.")


def record(kind, media_id, source):
    with open(LOG, "a", encoding="utf-8") as f:
        f.write(json.dumps({"date": today(), "time": datetime.datetime.now(IST).isoformat(timespec="seconds"),
                            "kind": kind, "media_id": media_id, "source": os.path.relpath(source, ROOT)}) + "\n")


# --- Cloudinary: Instagram only accepts media from a public URL ---

def cloudinary_signature(params, secret):
    return hashlib.sha1(("&".join(f"{k}={params[k]}" for k in sorted(params)) + secret).encode()).hexdigest()


def upload(path):
    resource = "video" if path.lower().endswith((".mp4", ".mov")) else "image"
    params = {"timestamp": str(int(time.time())), "folder": "the-early-pm"}
    params["signature"] = cloudinary_signature(params, os.environ["CLOUDINARY_API_SECRET"])
    mime = "video/mp4" if resource == "video" else "image/png"
    # shortcut: data-URI upload is capped near 100 MB by Cloudinary; switch to chunked upload if reels grow past that
    params["file"] = f"data:{mime};base64," + base64.b64encode(open(path, "rb").read()).decode()
    params["api_key"] = os.environ["CLOUDINARY_API_KEY"]
    url = f"https://api.cloudinary.com/v1_1/{os.environ['CLOUDINARY_CLOUD_NAME']}/{resource}/upload"
    return http("POST", url, params)["secure_url"]


def http(method, url, params):
    data = urllib.parse.urlencode(params).encode()
    req = urllib.request.Request(url if method == "POST" else f"{url}?{data.decode()}",
                                 data=data if method == "POST" else None, method=method)
    with urllib.request.urlopen(req, context=SSL, timeout=300) as r:
        return json.load(r)


# --- Scalekit Instagram connector ---

_actions = None


def tool(name, **tool_input):
    global _actions
    if _actions is None:
        from scalekit import ScalekitClient
        _actions = ScalekitClient(os.environ["SCALEKIT_ENVIRONMENT_URL"], os.environ["SCALEKIT_CLIENT_ID"],
                                  os.environ["SCALEKIT_CLIENT_SECRET"]).actions
    res = _actions.execute_tool(tool_name=name, tool_input=tool_input, identifier=identity(),
                                connection_name=os.environ.get("SCALEKIT_CONNECTION_NAME", "instagram"))
    return dict(res.data or {})


def identity():
    return os.environ.get("SCALEKIT_IDENTIFIER", "ceo")


def wait_ready(status_of, container_id):
    for _ in range(60):  # reels can take a few minutes to process
        code = status_of(container_id)
        if code == "FINISHED":
            return
        if code in ("ERROR", "EXPIRED"):
            sys.exit(f"Container {container_id} failed: {code}")
        time.sleep(10)
    sys.exit(f"Container {container_id} not ready after 10 min")


def sk_status(cid):
    return tool("instagram_media_container_status_get", container_id=cid).get("status_code")


def post(folder):
    guard("feed")
    if os.path.exists(os.path.join(folder, "POSTED.json")):
        sys.exit(f"Already posted: {folder}")
    ig = os.environ["IG_USER_ID"]
    caption = open(os.path.join(folder, "caption.txt"), encoding="utf-8").read().strip()
    video, slides = os.path.join(folder, "video.mp4"), sorted(glob.glob(os.path.join(folder, "slide-*.png")))
    if os.path.exists(video):
        cid = tool("instagram_media_container_create", ig_user_id=ig, media_type="REELS",
                   video_url=upload(video), caption=caption)["id"]
    elif len(slides) >= 2:
        kids = [tool("instagram_media_container_create", ig_user_id=ig, image_url=upload(s),
                     is_carousel_item=True)["id"] for s in slides[:10]]
        for k in kids:
            wait_ready(sk_status, k)
        cid = tool("instagram_media_container_create", ig_user_id=ig, media_type="CAROUSEL",
                   children=",".join(kids), caption=caption)["id"]
    else:
        sys.exit(f"No video.mp4 or 2+ slide-*.png in {folder}")
    wait_ready(sk_status, cid)
    media_id = tool("instagram_media_publish", ig_user_id=ig, creation_id=cid)["id"]
    json.dump({"media_id": media_id, "posted": datetime.datetime.now(IST).isoformat(timespec="seconds")},
              open(os.path.join(folder, "POSTED.json"), "w"))
    record("feed", media_id, folder)
    print(f"Posted {media_id}")


# --- Stories: the Scalekit connector cannot create them, so call Meta's Graph API directly ---

def story(path):
    guard("story")
    ig, token = os.environ["IG_USER_ID"], os.environ["IG_GRAPH_TOKEN"]
    url = upload(path)
    key = "video_url" if url.endswith((".mp4", ".mov")) else "image_url"
    cid = http("POST", f"{GRAPH}/{ig}/media", {"media_type": "STORIES", key: url, "access_token": token})["id"]
    wait_ready(lambda c: http("GET", f"{GRAPH}/{c}", {"fields": "status_code", "access_token": token})["status_code"], cid)
    media_id = http("POST", f"{GRAPH}/{ig}/media_publish", {"creation_id": cid, "access_token": token})["id"]
    record("story", media_id, path)
    print(f"Story posted {media_id}")


def insights(n=25):
    ig = os.environ["IG_USER_ID"]
    media = tool("instagram_media_list", ig_user_id=ig, limit=n,
                 fields="id,caption,media_type,media_product_type,timestamp,permalink").get("data", [])
    for m in media:
        try:
            rows = tool("instagram_media_insights_get", media_id=m["id"],
                        metric="reach,views,saved,shares,likes,comments,total_interactions").get("data", [])
            m["insights"] = {r["name"]: r["values"][0]["value"] for r in rows}
        except Exception as e:  # one bad metric/media must not lose the rest of the pull
            m["insights"] = {"error": str(e)[:200]}
    out = os.path.join(PRODUCT, "insights", f"{today()}.json")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    json.dump(media, open(out, "w", encoding="utf-8"), indent=1, ensure_ascii=False)
    print(f"Saved {len(media)} posts to {os.path.relpath(out, ROOT)}")


def auth():
    from scalekit import ScalekitClient
    actions = ScalekitClient(os.environ["SCALEKIT_ENVIRONMENT_URL"], os.environ["SCALEKIT_CLIENT_ID"],
                             os.environ["SCALEKIT_CLIENT_SECRET"]).actions
    name = os.environ.get("SCALEKIT_CONNECTION_NAME", "instagram")
    actions.get_or_create_connected_account(connection_name=name, identifier=identity())
    print(actions.get_authorization_link(connection_name=name, identifier=identity()).link)


if __name__ == "__main__":
    load_env()
    cmd, args = (sys.argv[1:2] or ["help"])[0], sys.argv[2:]
    {"auth": auth, "post": lambda: post(os.path.abspath(args[0])), "story": lambda: story(os.path.abspath(args[0])),
     "insights": lambda: insights(int(args[0]) if args else 25)}.get(cmd, lambda: print(__doc__))()
