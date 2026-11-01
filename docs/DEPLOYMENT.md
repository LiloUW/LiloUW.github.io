# Hosting, building and publishing

How the site is hosted, how to build it locally, how changes go live, and what to do when something fails. For what to change and how, see [HOW_TO.md](HOW_TO.md).

## Hosting

| | |
| --- | --- |
| Repository | `LiloUW/LiloUW.github.io` on GitHub (public), branch `main` |
| Build | GitHub Pages, "Deploy from a branch": `main`, folder `/ (root)`. GitHub runs Jekyll itself (its own `github-pages` gem versions); nothing is built or committed by hand. |
| Addresses | https://pozzorg.com (custom domain) and https://LiloUW.github.io |
| Time to go live | 1–2 minutes after a push; browsers and GitHub's CDN may cache files for up to 10 minutes (hard-refresh with Cmd+Shift+R) |
| Deploy status | the repository's Actions tab, or `gh run list` / `gh run view <id>` |

### The pozzorg.com domain

- Registered at **Wix**, with DNS also managed at Wix (name servers `ns10`/`ns11.wixdns.net`).
- Apex `pozzorg.com`: four A records to GitHub Pages, `185.199.108.153`, `185.199.109.153`, `185.199.110.153`, `185.199.111.153`.
- `www.pozzorg.com`: CNAME to `lilouw.github.io`.
- The `CNAME` file in the repository holds `pozzorg.com`. Don't delete or rename it, or the custom domain stops working.
- In GitHub → Settings → Pages, the custom domain is `pozzorg.com` and "Enforce HTTPS" should be on once the certificate is issued.
- The domain must stay disconnected from the old Wix *site* (keep only Wix DNS), or Wix may restore its own records.
- The domain has no MX records, so there is no `@pozzorg.com` email.
- To diagnose: `gh api repos/LiloUW/LiloUW.github.io/pages/health` and `dig pozzorg.com @ns10.wixdns.net`.

## Building locally

`_scripts/build.sh [output folder]` builds the site the way GitHub Pages does (default output `/tmp/pozzo-site`) and runs `_scripts/check_site.py` on the result. Preview it with `python3 -m http.server 8000 -d /tmp/pozzo-site` and open http://localhost:8000.

- The script uses `_scripts/local-build/Gemfile`, which pins `github-pages` 227 and a few dependencies (`ffi < 1.17`, `nokogiri < 1.14`, `public_suffix < 5`, `activesupport < 7`, `zeitwerk < 2.7`, `concurrent-ruby < 1.3.5`, `webrick`) so it runs on the Mac's system Ruby 2.6, which is too old for the current gems.
- Gems are installed on the first run into `~/.cache/pozzo-site-gems` (outside the repository; set `BUNDLE_PATH` to use another folder). The first run needs internet access and takes a few minutes.
- With a modern Ruby (3.x) you can instead use the root `Gemfile`: `bundle install`, then `bundle exec jekyll serve` (live preview at http://localhost:4000).
- The build needs `LANG=en_US.UTF-8` (the script sets it); without it Jekyll fails on non-ASCII characters.

`_scripts/check_site.py <built site>` checks every internal link and image path case-sensitively (as GitHub Pages serves them) and reports images that break the proportion and size rules in [SITE_GUIDE.md](SITE_GUIDE.md) §4. It exits with an error if any link is broken.

## Publishing

1. Build and check (above), and look at the changed pages on desktop and phone widths.
2. Commit and push to `main`, from the terminal, GitHub Desktop, or GitHub's web editor.
3. Watch the deploy in the Actions tab (`gh run list`), then check the live page.

## Troubleshooting

Check [githubstatus.com](https://www.githubstatus.com) first: many failures are GitHub incidents (there were several in October 2026).

| Symptom | Meaning | Fix |
| --- | --- | --- |
| Push: `remote rejected … (Internal Server Error)` | GitHub server fault | Wait for the incident to clear, then push again |
| Push/fetch: `Could not resolve host: github.com` | Local network drop | Retry when online |
| Push rejected: file over 100 MB | GitHub's file-size limit | Compress the file (videos: `avconvert -p PresetAppleM4V480pSD`) or host it on YouTube |
| Deploy: `job was not acquired by Runner` | GitHub Actions outage | `gh run rerun <id>` or push again |
| Deploy fails in the build step | Usually a YAML error in front matter or a `_data` file | Run `_scripts/build.sh` locally; it shows the file and line |
| Image or link works locally but not online | Capitalization mismatch (macOS ignores case, GitHub doesn't) | `check_site.py` lists it; rename with `git mv` via a temporary name |
| Page still shows the old version | Caching | Wait up to 10 minutes or hard-refresh |
| GitHub Desktop errors | Details are in `~/Library/Application Support/GitHub Desktop/logs/<date>.desktop.production.log` | Read the log before guessing |
| Custom domain shows an error or "DNS check unsuccessful" | DNS not pointing at GitHub, or old records cached | Check the records above at Wix; wait for caches, then "Check again" in Settings → Pages |
