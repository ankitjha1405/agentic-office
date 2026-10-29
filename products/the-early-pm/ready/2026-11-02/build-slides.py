import subprocess, sys, pathlib, tempfile
OUT = pathlib.Path(sys.argv[1]); TMP = pathlib.Path(tempfile.mkdtemp())
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
HANDLE = "@theearlypm"  # placeholder, flagged in CHECKLIST.md
M = "Masai School, Product manager salary in India 2026"
F = "Futurense, Product manager salary in India"
# (kicker, headline, body, source)
S = [
 ("", "PM PAY<br>IN INDIA,<br>BY LEVEL", "Four ranges, with sources.", ""),
 ("", "Most freshers guess their number.", "Check an offer against these ranges&nbsp;first.", ""),
 ("APM", "₹8-22 LPA", "About 0-2 years of experience.", M),
 ("PM", "₹20-40 LPA", "About 2-5 years of experience.", M),
 ("SENIOR PM", "₹35-60 LPA", "About 5-8 years of experience.", "Masai School, 2026 market estimates"),
 ("AI PM", "₹25-60 LPA", "Same job, plus AI skills on the posting.", F),
 ("", "Read these as ranges, not offers.", "Both pages are content-marketing estimates. Company, city and stage will move your number.", ""),
 ("RECAP", "PM pay in India", "", "Sources: Masai School, Futurense"),
 ("", "Save this for your next offer call.", "", ""),
]
RECAP = [("APM","₹8-22 LPA"),("PM","₹20-40 LPA"),("Senior PM","₹35-60 LPA"),("AI PM","₹25-60 LPA")]
CSS = """*{margin:0;box-sizing:border-box}html,body{width:1080px;height:1350px;overflow:hidden}
body{background:#0f1115;color:#f4f1ea;font-family:-apple-system,'Helvetica Neue',Helvetica,Arial,sans-serif;position:relative}
.wrap{position:absolute;left:120px;right:120px;top:120px;bottom:120px;display:flex;flex-direction:column;justify-content:center}
.num{position:absolute;top:56px;right:120px;font-size:32px;color:#9aa0aa;font-weight:600}
.brand{position:absolute;top:56px;left:120px;font-size:32px;color:#ffb547;font-weight:700;letter-spacing:.04em}
.kick{font-size:44px;font-weight:800;color:#ffb547;letter-spacing:.06em;margin-bottom:28px}
h1{font-size:84px;line-height:1.08;font-weight:800;letter-spacing:-.01em}
h1.big{font-size:150px}
h1.cover{font-size:118px;line-height:1.02}
p{font-size:48px;line-height:1.3;color:#c9ccd2;margin-top:40px}
.bar{width:120px;height:12px;background:#ffb547;margin-bottom:48px}
.foot{position:absolute;left:120px;right:120px;bottom:56px;display:flex;justify-content:space-between;align-items:flex-end;gap:40px;font-size:32px;color:#9aa0aa}
.foot .src{max-width:620px;line-height:1.25}.foot .h{color:#f4f1ea;font-weight:600;white-space:nowrap}
table{margin-top:48px;border-collapse:collapse;width:100%}td{font-size:54px;padding:22px 0;border-bottom:2px solid #2a2e36}
td.v{text-align:right;font-weight:800;color:#ffb547}"""
for i,(k,h,b,src) in enumerate(S,1):
    cls = "cover" if i==1 else ("big" if k and k!="RECAP" else "")
    body = f'<div class="bar"></div>' + (f'<div class="kick">{k}</div>' if k and k!="RECAP" else "") + f'<h1 class="{cls}">{h}</h1>'
    if b: body += f"<p>{b}</p>"
    if k=="RECAP": body += "<table>" + "".join(f'<tr><td>{a}</td><td class="v">{v}</td></tr>' for a,v in RECAP) + "</table>"
    html = f'<!doctype html><meta charset="utf-8"><style>{CSS}</style><div class="brand">THE EARLY PM</div><div class="num">{i}/{len(S)}</div><div class="wrap">{body}</div><div class="foot"><div class="src">{("Source: "+src) if src and not src.startswith("Sources") else src}</div><div class="h">{HANDLE}</div></div>'
    f = TMP/f"s{i}.html"; f.write_text(html)
    subprocess.run([CHROME,"--headless=new","--disable-gpu","--hide-scrollbars","--force-device-scale-factor=1","--window-size=1080,1350",f"--screenshot={OUT}/slide-{i:02d}.png",f.as_uri()],check=True,capture_output=True)
print("ok")
