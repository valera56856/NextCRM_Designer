#!/usr/bin/env python3
"""Fetch all real (non-separator) pages of NextCRM Design System Figma file."""
import json, os, time, urllib.request, urllib.parse, sys, re

TOKEN = os.environ["FIGMA_TOKEN"]
FILE = "H1Ngineb53cAIqPWdqD585"
OUT = "/tmp/figma-dump/pages"
os.makedirs(OUT, exist_ok=True)

def slug(s):
    s = re.sub(r"[^\w\s\-]", "", s, flags=re.UNICODE).strip()
    s = re.sub(r"\s+", "-", s).lower()
    return s[:60] or "page"

def http_get(url):
    req = urllib.request.Request(url, headers={"X-Figma-Token": TOKEN})
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.loads(r.read())

# Step 1: list pages
data = http_get(f"https://api.figma.com/v1/files/{FILE}?depth=1")
pages = data["document"]["children"]

# Filter out separators and meta pages
SKIP_NAMES = {"Cover", "--", "---"}
real_pages = []
for p in pages:
    name = p["name"]
    if name in SKIP_NAMES: continue
    if "〰" in name: continue        # separator pages
    if name.startswith("📋"): continue  # changelog
    if name.startswith("ℹ️"): continue   # guidance
    if "Archive" in name: continue
    real_pages.append(p)

print(f"Will fetch {len(real_pages)} real pages out of {len(pages)} total")
manifest = []

# Step 2: fetch each page subtree with depth=3
for i, p in enumerate(real_pages, 1):
    pid = p["id"]
    pname = p["name"]
    fname = f"{i:02d}-{slug(pname)}.json"
    fpath = os.path.join(OUT, fname)
    if os.path.exists(fpath) and os.path.getsize(fpath) > 100:
        print(f"  [{i:2d}/{len(real_pages)}] skip (cached) {pname}")
        manifest.append({"id": pid, "name": pname, "file": fname})
        continue
    try:
        url = f"https://api.figma.com/v1/files/{FILE}/nodes?ids={urllib.parse.quote(pid)}&depth=3"
        d = http_get(url)
        with open(fpath, "w", encoding="utf-8") as f:
            json.dump(d, f, ensure_ascii=False)
        size_kb = os.path.getsize(fpath) // 1024
        print(f"  [{i:2d}/{len(real_pages)}] saved {pname} ({size_kb} KB)")
        manifest.append({"id": pid, "name": pname, "file": fname})
        time.sleep(0.4)  # rate limit gentle
    except Exception as e:
        print(f"  [{i:2d}/{len(real_pages)}] FAIL {pname}: {e}")
        manifest.append({"id": pid, "name": pname, "file": None, "error": str(e)})

with open(os.path.join(OUT, "_manifest.json"), "w", encoding="utf-8") as f:
    json.dump(manifest, f, ensure_ascii=False, indent=2)

print(f"\nDone. Manifest: {OUT}/_manifest.json")
