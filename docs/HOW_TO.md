# How to update the site: step-by-step recipes

Recipes for every common edit, for people and AI agents alike. The rules behind them (style, image proportions, writing conventions, fact checking) are in [SITE_GUIDE.md](SITE_GUIDE.md); read its **standing rules** first.

Every recipe ends the same way: **build and check** (last section), then commit and push (or, for an agent, stage and ask).

| I want to… | Edit | Recipe |
| --- | --- | --- |
| Add a news story | new file in `_posts/` + photos in `assets/img/news/<slug>/` | [News story](#add-a-news-story) |
| Add, move or update a person | `_data/people.yml` (+ headshot in `assets/img/people/`) | [People](#people) |
| Add a publication | `_data/publications.yml` | [Publications](#publications) |
| Change a research area | `_data/research.yml` (+ banner in `assets/img/research/`) | [Research areas](#research-areas) |
| Change a course | `_data/settings.yml` → `courses` | [Courses](#courses) |
| Change the CV page | `_data/cv/*.yml` | [CV](#cv) |
| Change page intro text | `_pages/<page>.md` | [Page text](#page-text) |
| Change the menu, home photo, "In the Lab" strip, footer icons, contact card | `_data/settings.yml` | [Site settings](#site-settings) |
| Add or change an interactive figure | `assets/interactive/` + `_data/settings.yml` | [Interactive figures](#interactive-figures) |
| Change the look | `_sass/main.scss`, `_layouts/`, `_includes/` | [Design changes](#design-changes) |

## Add a news story

Each story is one Markdown file in `_posts/`, named `YYYY-MM-DD-short-slug.md` (lowercase, hyphens). The date in the filename is the publication date. Stories appear newest first on `/news/`, and the three newest also appear on the home page. The story's address is `/news/YYYY/short-slug/`.

1. **Images.** Put them in `assets/img/news/<short-slug>/` as `01.jpg`, `02.jpg`, … Convert and resize first, because uploads are often AVIF/HEIC/PNG files with misleading extensions and full camera resolution:
   ```bash
   sips -s format jpeg -s formatOptions 85 -Z 1600 "<source image>" --out assets/img/news/<short-slug>/01.jpg
   ```
   `-Z 1600` sets the longest side to 1600 px, and sips will also *enlarge* smaller images, so first check the size with `sips -g pixelWidth -g pixelHeight <file>` and drop `-Z 1600` if the image is already smaller. Check with `file` that the result is real JPEG data. Raw uploads can sit in `Images/` (git-ignored, never published, never referenced).
2. **Post file.** Copy this template. Only `title` is required; delete the lines you don't need.
   ```markdown
   ---
   title: "Congratulations, Dr. Example!"
   image: /assets/img/news/<short-slug>/01.jpg          # large photo at the top of the story
   image_alt: "What the photo shows"                     # for screen readers
   image_caption: "Optional caption shown under the photo"
   thumbnail: /assets/img/news/defense.jpg             # square-cropped image in news lists; defaults to `image`
   gallery:                                              # extra photos shown in a grid below the text
     - image: /assets/img/news/<short-slug>/02.jpg
       caption: "Optional caption"
   ---

   First paragraph. It becomes the summary on the news list, so make it a complete sentence about the news.

   More paragraphs, with [links](https://example.com) in Markdown.
   ```
3. **Shared thumbnails.** Use `/assets/img/news/defense.jpg` (graduation cap) for dissertation defenses and `/assets/img/news/candidacy.jpg` (balloons) for candidacy/general exams. Keep the real group photo as `image`.
4. **Related updates.** A defense usually also means moving the person from `current` to `alumni` in `_data/people.yml` (see [People](#people)). A new paper goes in `_data/publications.yml`.
5. **Style.** Third person ("Brenden Pelkie successfully defended his dissertation, titled \"…\", on May 30th, 2025."), dissertation or talk titles in quotes, first name after the first mention, and a closing "Congratulations, Dr. X!" for defenses. **Never put ` | ` in story text**: Kramdown turns the line into a table and merges the links. Separate links with ` · `.

**Defense stories** follow the structure in SITE_GUIDE.md §5. Quote the dissertation title and link the dissertation in ResearchWorks, the UW Libraries archive: search `https://digital.lib.washington.edu/server/api/discover/search/objects?query=<surname>`, confirm the author and advisor, and link the `https://hdl.handle.net/1773/...` handle. Note any embargo (e.g. "restricted to UW users until 2028"). Dissertations appear 1–4 months after the defense; if it isn't there yet, publish without the link and add it later. If there's a defense announcement, add the location and put the abstract, verbatim, in a collapsible block after the research paragraph:

```html
<details class="mb-4" markdown="1">
<summary>Read the dissertation abstract</summary>

Abstract paragraph(s)...

</details>
```

**Finding social posts:** LinkedIn posts can't be found by searching. Profile and activity pages return HTTP 999 or a login wall, and search engines don't index posts. A post is only reachable through its direct link, so **ask the site owner for the LinkedIn link**. Prof. Pozzo's Bluesky (`lilopozzo.bsky.social`) is public and can be scanned by date: `https://public.api.bsky.app/xrpc/app.bsky.feed.getAuthorFeed?actor=lilopozzo.bsky.social&limit=100` (page with `cursor`; full-size photos are under `embed.images[].fullsize`). Bluesky's search endpoint needs a login. A LinkedIn post's date is encoded in its ID: `(activity_id >> 22) / 1000` gives Unix seconds; public posts expose their photos in the page HTML (`media.licdn.com/.../feedshare-...`). Identify only people the source names.

## People

All in `_data/people.yml`; field meanings are in SITE_GUIDE.md §2.

- **New member:** add an entry under the right `current` group with `name`, `role`, `research`, `image` and any links. Add a square (1:1) headshot at `assets/img/people/firstname-lastname.jpg`, about 800 × 800 px; crop non-square photos around the face and keep the original in `_sources/images/people/`.
- **Graduate or leaves:** move the entry to the right `alumni` group, add "(Ph.D. YEAR)" to `name`, delete `image` and the headshot file, and add `now:` (current position, verified) when known. `now_url:` links the position, e.g. to a company page.
- **New position for an alum:** set `now:` (e.g. `'Engineer, Intel'`); write "Incoming …" for a position not yet started.

## Publications

`_data/publications.yml`, newest first, `number` counting up (the newest has the highest number).

- Author format `H.T. Chiang, L.D. Pozzo`; journal format `Journal, vol(issue), pages (year)`; link through `https://doi.org/...`. Confirm the DOI on Crossref (`https://api.crossref.org/works/<doi>`): same title, Pozzo among the authors.
- Add `corresponding: true` when Prof. Pozzo is a corresponding author (verify it; SITE_GUIDE.md §6). The home page automatically features the six newest such papers.
- Add `open_access: true` only for fully open-access journals, per the DOAJ rule in SITE_GUIDE.md §5.
- Optional table-of-contents graphic: see IMAGES_GUIDE.md.

## Research areas

`_data/research.yml`: one entry per area with `title`, `image` and `description`. The image is a **2.2:1 banner** in `assets/img/research/` (crop rules in SITE_GUIDE.md §4; keep the uncropped original in `_sources/images/research/`). The extra sections below the areas (Science Jubilee video, Hurricane Maria project) are written directly in `_pages/research.md`.

## Courses

`_data/settings.yml` → `courses`: `name`, `description` (leave `''` until the owner provides one), and optionally:
- `images:` a list of `{image, alt}` photo tiles, **3:4 upright**, in `assets/img/courses/` (originals in `_sources/images/courses/`);
- `figure: {src, title}`: an interactive figure shown in a square window under the description (the pipetting robot is under Surface & Colloid Science).

## CV

`_data/cv/`: `education.yml`, `academic-experience.yml`, `awards.yml`, `entrepreneurship.yml`, `service.yml`, each a list of `{title, description}`. Section order and headings are in `sections.yml`. The intro line is in `_pages/cv.md`. The full CV PDF (`_sources/documents/`) is a reference for facts and is never published.

## Page text

Each page is a Markdown file in `_pages/` (`index.md` is the home page). Edit the text below the `---` front matter. Keep each file's `layout` and `permalink` lines unchanged; they set the template and the web address. The People page's bottom text ("Undergraduate Researchers", "Join Our Team") is the `footer:` block in the front matter of `_pages/people.md`.

## Site settings

`_data/settings.yml`:
- `menu`: name and url of each menu item (lowercase single words; must fit on one line at 1280 px).
- `home_image`: the group photo on the home page.
- `home_figures`: interactive figures under the group photo (see below).
- `gallery`: the home page "In the Lab" strip; 2.2:1 images in `assets/img/lab/`.
- `social`: footer icons (Font Awesome 5 names). No Twitter/X.
- `contacts`: the contact-page card.

Site-wide facts (title, tagline, description, author block) are in `_config.yml`.

## Interactive figures

1. Put the self-contained HTML "web version" in `assets/interactive/<name>.html` (lowercase-hyphen, no front matter). Read and safety-check the whole file first (SITE_GUIDE.md §4, "Interactive figures").
2. Show it on the home page by adding `{src, title}` to `home_figures` in `_data/settings.yml` (an optional `caption` shows text underneath; currently none; `left` shifts an off-centre figure inside its square window; `wide: true` gives a long figure a trimmed 5:4 window). Or show it under a course with `figure:` (see [Courses](#courses)).
3. Keep the editable sources in `_sources/interactive/<name>/` with a README saying how to rebuild. The SAXS instrument rebuilds with `python3 _sources/interactive/saxs-instrument/make_web.py`, which regenerates both `assets/interactive/saxs-instrument.html` (embedded) and `saxs-instrument-interactive.html` (full version).

## Design changes

Colours, spacing and component classes are in `_sass/main.scss` (tokens and classes are listed in SITE_GUIDE.md §3). Page templates are in `_layouts/` (one per page type) and shared pieces in `_includes/` (header, footer, news item, publication entry, person links, SEO tags). Change these only when the design itself is changing, and screenshot every affected page.

## Build and check (every change)

```bash
_scripts/build.sh                      # builds into /tmp/pozzo-site and runs the link/image check
python3 -m http.server 8000 -d /tmp/pozzo-site    # then open http://localhost:8000
```

The script builds the site the way GitHub Pages does and then runs `_scripts/check_site.py`, which catches broken or wrong-case links and off-ratio or oversized images. Look at every changed page at desktop width and on a phone (or a ~520 px window). Then commit and push to `main`; the live site updates in 1–2 minutes. Setup details and troubleshooting are in [DEPLOYMENT.md](DEPLOYMENT.md).
