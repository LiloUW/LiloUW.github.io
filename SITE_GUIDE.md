# Pozzo Research Group Website: Rules and Style Guide

This is the reference for anyone, human or AI agent, updating this website. It records how the site is built, the visual and writing conventions, and the rules that keep it working. **Read it before making changes.** Step-by-step recipes for common tasks (adding a news story, a person, a paper) are in [CLAUDE.md](CLAUDE.md); every image slot is listed in [IMAGES_GUIDE.md](IMAGES_GUIDE.md).

## Standing rules from the site owner

These are explicit requests from Prof. Pozzo's group. Follow them on every update; details are in the sections referenced.

1. **Featured publications** on the home page are always the **six newest papers where Prof. Pozzo is a corresponding author**, chosen automatically from `corresponding: true` flags (§4).
2. **Open Access badge** only for papers in fully open-access journals (DOAJ-listed, published on or after the journal's open-access start year), e.g. ACS "Au" journals and Digital Discovery (§4).
3. **Every publication link must be verified:** the DOI resolves to the same title with Pozzo as an author (§4).
4. **Images in the same place share one proportion:** research/lab banners 2.2:1, headshots 1:1, course photos 3:4, news galleries in uncropped 4:3 frames. **Crop as little as possible** (combine or pad instead), and never cut faces or figure text (§3).
5. **No Twitter/X anywhere:** no links, icons, mentions or meta tags (§2).
6. **Lowercase-hyphen file names** that match references exactly; the live site is case-sensitive (§3).
7. **Never invent facts** (dates, titles, positions, course descriptions); leave them out and ask (§4).
8. **Check before reporting done:** build, run `_scripts/check_site.py`, and screenshot changed pages (§5).
9. **Don't commit or push without asking.** The owner often pushes changes themselves, so start with `git pull --ff-only` (§5).
10. **Alumni are listed without photos**, and the full CV PDF is not published (§6).

## 1. How the site works

| | |
| --- | --- |
| Live address | https://pozzorg.com (also https://LiloUW.github.io) |
| Hosting | GitHub Pages, built automatically from the `main` branch of `LiloUW/LiloUW.github.io` |
| Generator | Jekyll (GitHub Pages' built-in version), no theme gem (`theme: null`) |
| Design base | The "academic" Jekyll theme by Paul Le (MIT, see `THEME_LICENSE.txt`), copied into `_layouts/` and `_includes/` and customized |
| Libraries | Bootstrap 5 and Font Awesome 5.15 (bundled in `assets/libs/`) |
| Domain | `pozzorg.com`, registered at Wix with DNS managed at Wix. The apex A records point to GitHub (185.199.108–111.153), `www` is a CNAME to `lilouw.github.io`, and the `CNAME` file in the repo holds `pozzorg.com`. |

**Content lives in data files, not HTML.** To change what the site says, edit:

| Content | File |
| --- | --- |
| Menu, home image, "In the Lab" strip, courses, footer icons, contact card | `_data/settings.yml` |
| Research areas | `_data/research.yml` |
| Current members and alumni | `_data/people.yml` |
| Publications | `_data/publications.yml` |
| CV sections | `_data/cv/*.yml` (order in `_data/cv/sections.yml`) |
| News stories | `_posts/YYYY-MM-DD-slug.md` |
| Intro text of each page | `index.md`, `news.md`, `research.md`, `people.md`, `publications.md`, `courses.md`, `cv.md`, `contact.md` |

Pages and their addresses: `/` home, `/news/`, `/research/`, `/people/`, `/publications/`, `/courses/`, `/cv/`, `/contact/`, plus `/people/lilo-pozzo/` and one page per news story at `/news/YYYY/slug/`. Old addresses redirect: `/students/` → `/people/`, `/about/` → `/contact/`, and the old Wix `/post/<slug>/` links go to the matching story.

## 2. Visual style

Keep the look clean, white and minimal, as in the academic theme. Don't add new colors, fonts or decorative elements.

- **Colors:** black text on white. Links are dark gray (`#212529`) and turn **UW purple `#4b2e83`** on hover. UW purple is the only accent color: section underlines, the "Open Access" badge, and placeholder images.
- **Fonts:** the system font stack defined in `_sass/main.scss`. Body text stays at Bootstrap's default size.
- **Page width:** one centered column (`col-lg-8`), with a 16 px or larger side gutter on phones.
- **Section headings:** `<h3 class="fw-bold border-bottom pb-3 mb-5">`, giving bold text with a thin purple rule underneath. Sub-headings inside sections are `h4`/`h5` bold.
- **Menu:** lowercase single words (`news research people publications courses cv contact`). The current page is shown in bold. The menu must fit on one line at desktop width; check this when adding an item.
- **Two-column rows:** text beside an image (Bootstrap `row` with `col-md-6`/`col-md-7`). On the Research page the image side alternates left and right.
- **Icons:** Font Awesome 5 only. Google Scholar uses `fas fa-graduation-cap` (FA5 has no Scholar icon), and ORCID `fab fa-orcid`.
- **Footer:** department and university on the left; icons for Google Scholar, ORCID, LinkedIn and GitHub on the right.
- **No Twitter/X anywhere:** no icons, links, mentions, or `twitter:` meta tags. The SEO plugin was replaced with `_includes/seo.html` for exactly this reason, so don't re-enable `jekyll-seo-tag`.

## 3. Images

### Shape rules

Images in the same place must have the same proportions. Each slot has a standard ratio:

| Where | Ratio | Typical size | How it's shown |
| --- | --- | --- | --- |
| Research areas, home "In the Lab" strip, Research page banners | **2.2 : 1** | 1000–1320 × 455–600 px | Whole image, max 320 px tall (`.research-image`) |
| People headshots | **1 : 1** | 800 × 800 px | `.person-photo` |
| Course photos | **3 : 4** (upright) | ≤600 px wide | Row of equal tiles under each course (`.course-photo`); list them under `images:` in `_data/settings.yml` |
| News thumbnails (lists) | 1 : 1 | any | Cropped to square by CSS (`.news-thumb`) |
| News story galleries | **4 : 3 frame** | ≤1600 px long side | Whole image inside a 4:3 frame with a pale purple background (`.gallery-frame`), so portrait photos and flyers are never cut |
| News story top photo | natural | ≤1600 px long side | Whole image, max 600 px tall |
| Home group photo | ~2 : 1 | 1600 px wide | Whole image |
| Contact portrait | 4 : 5 | 900 × 1125 px | Whole image |
| Science Jubilee video poster | 1 : 1 | matches the square video | Video poster |

### Cropping policy

- **Crop as little as possible.** Pick the ratio that most images already have, and center the crop on the subject rather than the middle of the frame if needed (e.g. the Jubilee poster is anchored at 42% so the colored vials stay in).
- **Combine instead of cropping** when photos have awkward shapes: place two side by side to fill a 2.2:1 banner. The Hurricane Maria section uses a landscape banner (`hurricane-maria.jpg`) plus a banner of two upright photos (`hurricane-maria-team.jpg`), and many of the lab images are two-photo composites in the same style.
- **Repeating patterns can take bigger crops** (the gold well plate keeps 3 of 6 rows); faces, text and flyers cannot.
- **Keep the uncropped original** in `_image_sources/`, mirroring the `assets/img/` path, before cropping. Jekyll doesn't publish folders starting with `_`.

### File rules

- **Names:** lowercase, words separated by hyphens, `.jpg` (PNG only when transparency is needed), for example `assets/img/people/firstname-lastname.jpg`. **Capitalization must match exactly.** macOS ignores case but GitHub Pages doesn't, so `Kevin-lee.jpg` works locally and breaks online. To fix a case-only rename on a Mac, go through a temporary name or use `git mv`.
- **Formats:** uploads saved from the web are often AVIF or WebP with a `.png`/`.jpg` extension. Check with `file <name>` and convert (`sips -s format jpeg ...` or Pillow).
- **Size:** at most 1600 px on the long side, about 1 MB or less, JPEG quality ~85. Don't upscale small images (`sips -Z` enlarges them).
- **Video:** compress (macOS: `avconvert -p PresetAppleM4V480pSD`) or embed from YouTube. GitHub rejects files over 100 MB.
- **Alt text:** describe what the image shows, not its file name.
- **Placeholders:** purple-striped labeled images (camera icon, slot name, file path, size) generated with Pillow. None are in use as of October 2026; use the same style if a new slot needs one.
- **Raw uploads** go in `Images/`, which is git-ignored and never published or referenced.

## 4. Writing and content style

- **Voice:** clear, factual, third person for the group ("The Pozzo Research Group develops…", "our team"). No marketing superlatives.
- **Names:**
  - Full name on first mention, first name after that ("Brenden Pelkie… Brenden").
  - Prof. Pozzo is "Lilo D. Pozzo" or "Prof. Pozzo".
  - Her legal name changed in 2013 from D.C. Pozzo to L.D. Pozzo. Both forms (and "L. Pozzo") appear in author lists and are bolded automatically.
  - Use they/them for anyone whose pronouns aren't known.
- **Dates:** "May 30th, 2025" in story text; filenames and data use ISO dates.
- **News stories:**
  - The first paragraph must work alone as the summary on the news list.
  - Dissertation and talk titles go in quotes.
  - Defenses close with "Congratulations, Dr. X!" and use the shared graduation-cap thumbnail; candidacy exams use the balloons thumbnail.
- **People entries:**
  - `role` is the program and expected year for students.
  - `now:` is the current position for alumni ("Currently: …"); use "Incoming …" for positions not yet started.
  - `note:` holds co-advisors and previous positions.
- **Publications:**
  - Newest first, numbered consecutively (the newest has the highest number).
  - Authors as initials then surname (`H.T. Chiang, L.D. Pozzo`).
  - Journal as `Journal, vol(issue), pages (year)`, linked via `https://doi.org/...`.
  - **Home page "Featured Publications" = the six newest papers where Prof. Pozzo is a corresponding author.** This is automatic: mark each such paper `corresponding: true`, and `_includes/publications.html` shows the newest six. Don't hand-pick papers or add `featured` flags.
  - **Deciding `corresponding: true`:** use the corresponding-author marking on the publisher's page or PDF (the asterisk or envelope icon), or OpenAlex (`api.openalex.org/works/doi:<doi>` → `authorships[].is_corresponding`). Being last author is *not* proof. If neither source says, ask the site owner. Status has been checked for papers #91 and newer; #111 and #108 are awaiting the owner's confirmation.
  - Only peer-reviewed journal articles go in; no abstracts, patents, theses or preprints.
  - Check titles, authors and DOIs against Crossref (`api.crossref.org/works/<doi>`) or the publisher, not just Google Scholar, which truncates author lists and sometimes misattributes papers.
  - **Every DOI must resolve to the paper it's listed under.** In October 2026, 59 of 120 links were wrong (dead or pointing to unrelated papers) and were corrected. Before adding or editing an entry, confirm that `api.crossref.org/works/<doi>` returns the same title with Pozzo among the authors.
  - **Open Access badge (`open_access: true`):** mark a paper only if its journal is fully (gold) open access in the [DOAJ](https://doaj.org) **and** the paper's year is on or after the journal's DOAJ `oa_start` year. Current list: Digital Discovery (2022+), all ACS "Au" journals (e.g. ACS Polymers Au, 2021+), npj Computational Materials, Nature Communications, Photoacoustics (2013+), Ultrasonics Sonochemistry (2021+), Journal of Open Hardware, Journal of Open Source Software. Advanced Materials Interfaces became open access only in 2023, so its 2016 paper is not marked. Hybrid journals are not marked, even when an individual article happens to be free.
- **Never invent facts:** dates, positions, graduation years, job titles. If something is unknown, leave it out or ask, and flag any assumption to the site owner.

## 5. Making and checking changes

1. **Sync first:** `git pull --ff-only`. The site owner often commits and pushes directly, from this Mac or GitHub's web editor.
2. Make the change in the data file or post, following the rules above.
3. **Build locally:** see CLAUDE.md, "Building locally". The Mac's system Ruby is too old for the current gems, so the build uses a separate pinned Gemfile.
4. **Check:** `python3 _scripts/check_site.py <built _site>`. It flags broken links (case-sensitive), off-ratio images and files over 1 MB, and exits with an error if any link is broken.
5. **Look at it:** screenshot the changed pages at desktop width and about 520 px (narrow/phone). Headless Chrome cannot render narrower than ~500 px.
6. **Commit and push only when the site owner asks.** Pushing to `main` publishes the site within a minute or two.
7. **After a push:** `gh run list` shows the Pages deploy. A deploy that fails with "job was not acquired by Runner" is a GitHub outage, not a site error; re-run it or push again.

## 6. Decisions on record

- Rebuilt from a Wix site (pozzorg.com) on the academic theme in October 2026; old news stories and images were carried over.
- Twitter/X removed entirely at the owner's request; `jekyll-seo-tag` replaced by `_includes/seo.html` (Open Graph tags only).
- Research and lab images standardized to 2.2:1, headshots to 1:1, course photos to 3:4; news galleries use uncropped 4:3 frames.
- The full CV PDF is intentionally not published (`*.pdf` is excluded from the build).
- Alumni are listed without photos.
