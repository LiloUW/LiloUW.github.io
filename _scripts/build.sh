#!/bin/bash
# Build the site locally the way GitHub Pages does, then run the link and image check.
#
#   _scripts/build.sh [output folder]          (default: /tmp/pozzo-site)
#
# Gems are installed once, outside the repo, in ~/.cache/pozzo-site-gems (override with BUNDLE_PATH).
# Preview the result with:  python3 -m http.server 8000 -d <output folder>   then open http://localhost:8000
set -euo pipefail
cd "$(dirname "$0")/.."
OUT="${1:-/tmp/pozzo-site}"
export BUNDLE_GEMFILE="$PWD/_scripts/local-build/Gemfile"
export BUNDLE_PATH="${BUNDLE_PATH:-$HOME/.cache/pozzo-site-gems}"
export LANG=en_US.UTF-8 LC_ALL=en_US.UTF-8
export PAGES_REPO_NWO=LiloUW/LiloUW.github.io
bundle check >/dev/null 2>&1 || bundle install
rm -rf "$OUT"
bundle exec jekyll build -d "$OUT"
python3 _scripts/check_site.py "$OUT"
