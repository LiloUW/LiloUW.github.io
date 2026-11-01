# Pozzo Research Group website: instructions for AI agents

Jekyll site served by GitHub Pages from `main` (https://pozzorg.com, also https://LiloUW.github.io). Layouts are adapted from the "academic" theme by Paul Le. Most content is in YAML under `_data/`, pages are in `_pages/`, news stories in `_posts/`.

## Read first

1. **[docs/SITE_GUIDE.md](docs/SITE_GUIDE.md)**: the rulebook. Its **standing rules from the site owner** (top of the file) apply to every update; the numbered sections cover how the site works, data fields, visual style, image proportions and cropping, writing conventions, sources and verification, and the check-and-publish workflow.
2. **[docs/HOW_TO.md](docs/HOW_TO.md)**: step-by-step recipes (news story, people, publications, research, courses, CV, settings, interactive figures, design). Read the recipe for your task before starting.
3. As needed: [docs/IMAGES_GUIDE.md](docs/IMAGES_GUIDE.md) (every image slot and its file) and [docs/DEPLOYMENT.md](docs/DEPLOYMENT.md) (hosting, domain, local build, troubleshooting).

## Every session

1. `git pull --ff-only`. The owner often commits and pushes directly, from this Mac or GitHub's web editor.
2. Change data files and posts, not layouts, unless the design itself is changing.
3. Verify every fact and link against a primary source; never fill gaps with guesses (dates, titles, positions, pronouns, course descriptions). Ask the owner instead.
4. Build and check with `_scripts/build.sh <scratch dir>`, which runs `_scripts/check_site.py`. Screenshot the changed pages at ~1280 px and ~520 px with headless Chrome (`--window-size=1280,1000`; it can't render narrower than ~500 px).
5. Stage the changes and **ask before committing or pushing**. Report anything assumed or unverified.

## Repository map

| Path | What it holds | Published? |
| --- | --- | --- |
| `_pages/` | One Markdown file per page (`index.md` = home); each sets `layout` and `permalink` | yes (via `include:` in `_config.yml`) |
| `_posts/` | News stories, `YYYY-MM-DD-slug.md` | yes, at `/news/YYYY/slug/` |
| `_data/` | Content: `settings.yml` (menu, home, courses, footer, contact), `people.yml`, `publications.yml`, `research.yml`, `cv/` | rendered into pages |
| `_layouts/`, `_includes/`, `_sass/` | Templates, shared pieces, styles | rendered into pages |
| `assets/` | Everything served as-is: `img/`, `interactive/`, `video/`, `css/`, `libs/`, icons | yes |
| `_sources/` | Originals: uncropped images (`images/`, mirroring `assets/img/`), interactive-figure source code (`interactive/<name>/`), reference documents (`documents/`, e.g. the CV PDF) | no |
| `_scripts/` | `build.sh` (local build + check), `check_site.py` (link and image checker), `local-build/Gemfile` | no |
| `docs/` | Guides for people and agents | no |
| `Images/` | Raw uploads from the owner; git-ignored; never reference it | no |
| `_config.yml`, `CNAME`, `Gemfile` | Site settings, custom domain, GitHub Pages gem | config |

## Gotchas

- **File names are case-sensitive online.** macOS ignores case, GitHub Pages doesn't. Use lowercase-hyphen names; rename via a temporary name or `git mv`; `check_site.py` catches mismatches.
- **No ` | ` in Markdown text** (Kramdown makes it a table). Use ` · ` between links.
- **Internal links in layouts and includes** use `{{ '/path/' | relative_url }}`.
- **A new page** goes in `_pages/` and must set `permalink:`; without it the address would start with `/_pages/`.
- **Keep the site light:** images under ~1 MB and ≤1600 px; compress videos (`avconvert -p PresetAppleM4V480pSD`) or use YouTube. GitHub rejects files over 100 MB.
- **No Twitter/X** links, icons or meta tags, anywhere.
- **LinkedIn can't be searched or scraped**: ask the owner for direct post or profile links, and don't try to get around its bot checks.
- A failed Pages deploy with "job was not acquired by Runner" is a GitHub outage: `gh run rerun <id>` or push again.
