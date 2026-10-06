#!/usr/bin/env python3
"""Check a built Jekyll site the way GitHub Pages serves it.

Usage: python3 _scripts/check_site.py <path to built _site>

- Every internal src/href/poster link must point to a file that exists with the
  exact same capitalization (macOS ignores case, GitHub Pages does not).
- Reports images that break the size and proportion rules in SITE_GUIDE.md.
Exits with status 1 if any link is broken.
"""
import os
import re
import sys

site = sys.argv[1] if len(sys.argv) > 1 else "_site"
files = set()
for root, _, names in os.walk(site):
    for name in names:
        files.add(os.path.join(root, name)[len(site):].replace(os.sep, "/"))


def exists(path):
    path = path.split("#")[0].split("?")[0]
    return path in files or path.rstrip("/") + "/index.html" in files


refs = set()
for root, _, names in os.walk(site):
    for name in names:
        if name.endswith(".html"):
            with open(os.path.join(root, name), encoding="utf-8") as fh:
                refs |= set(re.findall(r'(?:src|href|poster)="(/[^"]*)"', fh.read()))

broken = sorted(p for p in refs if not exists(p))
print(f"{len(refs)} internal links checked; broken: {broken or 'none'}")

# Image rules (see SITE_GUIDE.md, "Images"): ratio groups and file size.
try:
    from PIL import Image
except ImportError:
    Image = None
    print("(Pillow not installed: skipping image checks)")
if Image:
    rules = {"/assets/img/research/": 2.2, "/assets/img/lab/": 2.2, "/assets/img/people/": 1.0, "/assets/img/courses/": 0.75}
    exempt = {"/assets/img/research/science-jubilee.jpg": 1.0}  # video poster matches the square video
    for path in sorted(files):
        if not path.startswith("/assets/img/") or path.endswith(".ico"):
            continue
        full = os.path.join(site, path.lstrip("/"))
        size_kb = os.path.getsize(full) / 1024
        if size_kb > 1024:
            print(f"  large file ({size_kb:.0f} KB): {path}")
        want = exempt.get(path) or next((r for prefix, r in rules.items() if path.startswith(prefix)), None)
        if want:
            w, h = Image.open(full).size
            if abs(w / h - want) / want > 0.03:
                print(f"  off-ratio ({w}x{h} = {w / h:.2f}, expected {want}): {path}")

sys.exit(1 if broken else 0)
