# Pozzo Research Group Website: Rules and Style Guide

This is the reference for anyone, human or AI agent, updating this website. It records how the site is built, its visual and writing conventions, where facts come from and how to verify them, and the rules that keep it working. **Read it before making changes.**

Companion files:
- [CLAUDE.md](CLAUDE.md): step-by-step recipes (adding a news story, person, paper; building locally). Claude Code loads it automatically.
- [IMAGES_GUIDE.md](IMAGES_GUIDE.md): every image slot on the site and its file.
- `_scripts/check_site.py`: the automated check to run before every publish.

*Last updated: October 8, 2026.*

## Before you start: checklist for every update

1. `git pull --ff-only`. The site owner often commits and pushes directly, from this Mac or GitHub's web editor.
2. Read the **standing rules** below and the section for the content you're changing.
3. Make the change in the data file or post, not in HTML layouts, unless the design itself is changing.
4. Verify every fact and link against a primary source (§6). Never fill gaps with guesses.
5. Build locally, run `python3 _scripts/check_site.py <built _site>`, and screenshot the changed pages (§8).
6. Stage the changes and **ask before committing or pushing**. Report anything you assumed or couldn't verify.

## Standing rules from the site owner

These are explicit requests from Prof. Pozzo's group. Follow them on every update; details are in the sections referenced.

1. **Featured publications** on the home page are always the **six newest papers where Prof. Pozzo is a corresponding author**, chosen automatically from `corresponding: true` flags (§5).
2. **Open Access badge** only for papers in fully open-access journals (DOAJ-listed, published on or after the journal's open-access start year), e.g. ACS "Au" journals and Digital Discovery (§5).
3. **Every publication link must be verified:** the DOI resolves to the same title with Pozzo as an author (§6).
4. **Images in the same place share one proportion:** research/lab banners 2.2:1, headshots 1:1, course photos 3:4, news galleries in uncropped 4:3 frames. **Crop as little as possible** (combine or pad instead), and never cut faces or figure text (§4).
5. **No Twitter/X anywhere:** no links, icons, mentions or meta tags (§3).
6. **Lowercase-hyphen file names** that match references exactly; the live site is case-sensitive (§4).
7. **Never invent facts** (dates, titles, positions, pronouns, course descriptions); leave them out and ask (§5).
8. **Defense news stories** quote the dissertation title, link the dissertation, and include the abstract when an announcement is available (§5).
9. **Check before reporting done:** build, run `_scripts/check_site.py`, and screenshot changed pages (§8).
10. **Don't commit or push without asking**, and start every session with `git pull --ff-only` (§8).
11. **Alumni are listed without photos**, and the full CV PDF is not published (§10).

## 1. How the site works

| | |
| --- | --- |
| Live address | https://pozzorg.com (also https://LiloUW.github.io) |
| Hosting | GitHub Pages, built automatically from the `main` branch of `LiloUW/LiloUW.github.io`, live 1–2 minutes after a push |
| Generator | Jekyll (GitHub Pages' built-in version, Kramdown Markdown), no theme gem (`theme: null`) |
| Plugins | `jekyll-feed` (RSS) and `jekyll-redirect-from` (old addresses). Not `jekyll-seo-tag` (§3). |
| Design base | The "academic" Jekyll theme by Paul Le (MIT, see `THEME_LICENSE.txt`), copied into `_layouts/` and `_includes/` and customized |
| Libraries | Bootstrap 5 and Font Awesome 5.15, bundled in `assets/libs/` |
| Domain | `pozzorg.com`, registered at Wix with DNS managed at Wix. The apex A records point to GitHub (185.199.108–111.153), `www` is a CNAME to `lilouw.github.io`, and the `CNAME` file in the repo holds `pozzorg.com`. |

### Pages and templates

| Address | Page file | Layout | Notes |
| --- | --- | --- | --- |
| `/` | `index.md` | `home.html` | Intro text (`col-md-5`) beside the group photo with the interactive figure beneath it (`col-md-7`), "In the Lab" strip, 3 latest news, 6 featured publications |
| `/news/` | `news.md` | `news.html` | All stories, newest first (`_includes/news-item.html`) |
| `/news/YYYY/slug/` | `_posts/*.md` | `post.html` | One page per story |
| `/research/` | `research.md` | `research.html` | Research areas from `_data/research.yml`, then the page text |
| `/people/` | `people.md` | `people.html` | Current members (photo cards), alumni (list); footer text in front matter |
| `/people/lilo-pozzo/` | `people/lilo-pozzo.md` | `page.html` | PI profile |
| `/publications/` | `publications.md` | `publications.html` | Grouped by year (`_includes/publications.html` + `publication.html`) |
| `/courses/` | `courses.md` | `courses.html` | Courses, photo tiles and interactive figures from `_data/settings.yml` |
| `/cv/` | `cv.md` | `cv.html` | Sections from `_data/cv/` |
| `/contact/` | `contact.md` | `contact.html` | Contact card + "Join the Group" |

Old addresses redirect: `/students/` → `/people/`, `/about/` → `/contact/`, and the old Wix `/post/<slug>/` links go to the matching story (via `redirect_from`).

Folders starting with `_` are never published: `_image_sources/` (uncropped originals), `_scripts/`. Neither are `Images/` (raw uploads, also git-ignored), the `.md` guides, or any `*.pdf`.

## 2. Where content lives (data files and fields)

**Content lives in data files, not HTML.** Fields marked *optional* can be omitted.

**`_data/settings.yml`**: `menu` (name, url), `home_image` (image, alt), `home_figures` (interactive figures stacked under the group photo at its width: src, title, *optional* caption, `left` offset, and `wide: true` for a 5:4 window; remove an entry to hide it), `gallery` ("In the Lab": image, caption), `courses` (name, description, *optional* `images` and `figure: {src, title}`), `social` (footer icons: icon, title, link), `contacts` (contact card).
- Course: `name`, `description` (may be `''`), *optional* `images:` list of `{image, alt}` tiles, *optional* `url`.

**`_data/research.yml`**: one entry per research area: `title`, `image` (2.2:1 banner), `description`.

**`_data/people.yml`**: `current` and `alumni`, each a list of groups `{title, members}`. Member fields:

| Field | Use |
| --- | --- |
| `name` | Alumni include the degree and year: `'Claire Benstead (Ph.D. 2026)'` |
| `role` | Current members: program and expected year, e.g. `'Chemical Engineering Ph.D. (expected 2028)'` |
| `research` | One line, sentence case, no final period |
| `image` | Current members only: `assets/img/people/firstname-lastname.jpg` |
| `now` | Alumni: current position, shown as "Currently: …"; prefix "Incoming" for positions not yet started |
| `now_url` | Alumni, optional: link for the current position, e.g. a company page (`'https://membrion.com/'`) |
| `note` | Co-advisors, fellowships, previous positions |
| `linkedin`, `scholar`, `orcid`, `website` | Full URLs; shown as icons |
| `url` | Slug of a profile page in `people/` (only the PI has one) |

**`_data/publications.yml`**: newest first. Fields: `number`, `year`, `title`, `authors`, `journal`, `url` (DOI link), *optional* `open_access: true`, `corresponding: true`, `image` (TOC graphic). Rules in §5.

**`_data/cv/*.yml`**: `education`, `academic-experience`, `awards`, `entrepreneurship`, `service`, each a list of `{title, description}`; display order in `sections.yml`.

**`_posts/YYYY-MM-DD-slug.md`** (news): front matter `title` (required), *optional* `image`, `image_alt`, `image_caption`, `thumbnail`, `gallery` (list of `{image, caption}`), `redirect_from`. The filename date is the story date. Template in CLAUDE.md.

## 3. Visual style

Keep the look clean, white and minimal, as in the academic theme. Don't add new colors, fonts or decorative elements.

### Design tokens (`_sass/main.scss`)

| Token | Value | Used for |
| --- | --- | --- |
| Background | `#ffffff` | Page |
| Text | `#000000` | Body text |
| Links | `#212529` (dark gray), underlined | All links |
| **Accent: UW purple** | `#4b2e83` | Link hover, section-heading rules, "Open Access" badge, abstract toggles, placeholder images. The **only** accent color. |
| Pale purple | `#f3f1f7` | Background of news gallery frames |
| Font | System font stack (`-apple-system, Segoe UI, Helvetica, Arial…`) | Everything; Bootstrap default sizes |

### Layout conventions

- **Page width:** one centered column (`col-lg-8`), with a 16 px or larger side gutter on phones.
- **Section headings:** `<h3 class="fw-bold border-bottom pb-3 mb-5">`, giving bold text with a thin purple rule. Sub-headings are bold `h4`/`h5`.
- **Menu:** lowercase single words (`news research people publications courses cv contact`); the current page is bold. It must fit on one line at desktop width (1280 px), so check this when adding an item.
- **Two-column rows:** text beside an image (`row` with `col-md-6`/`col-md-7`). On the Research page the image side alternates left and right.
- **Icons:** Font Awesome 5 only. Google Scholar is `fas fa-graduation-cap` (FA5 has no Scholar icon), and ORCID `fab fa-orcid`.
- **Footer:** department and university on the left; Google Scholar, ORCID, LinkedIn and GitHub icons on the right.
- **No Twitter/X anywhere:** no icons, links, mentions, or `twitter:` meta tags. Page metadata comes from `_includes/seo.html` (title, description, Open Graph tags); don't re-enable `jekyll-seo-tag`, which adds Twitter tags.

### Components (CSS classes)

Reuse these instead of writing new styles.

| Class / element | What it does | Where |
| --- | --- | --- |
| `.research-image` | Pre-cropped 2.2:1 banner shown whole at full column width | Research areas, "In the Lab" (via `img-fluid`), Hurricane Maria banners |
| `.person-photo` | Square headshot (1:1, `object-fit: cover`) | People cards, PI page |
| `.course-photo` | Upright 3:4 tile | Courses page |
| `.news-thumb` | Square thumbnail, CSS-cropped | News lists (home and `/news/`) |
| `.news-hero` | Story's top photo, whole, max 600 px tall | Top of each story |
| `.gallery-frame` | Uniform 4:3 frame, image scaled to fit (never cropped), pale purple background | Galleries at the bottom of stories |
| `details > summary` | Collapsible block with a purple bold toggle | "Read the dissertation abstract" |
| `.open-access-badge` | Purple "Open Access" pill | Publications |
| `.publication-image` | Optional TOC graphic, 120 px wide | Publications |
| `.figure-embed` | Plain 4:3 frame (`<iframe sandbox="allow-scripts" loading="lazy">`) for an interactive figure | Available; not currently used |
| `.figure-crop` | Square window onto a 4:3 figure page: the page is drawn at the window's height and centered (nudged 3% right), trimming its empty sides so the figure fills the window; a figure's `left` setting overrides the offset | Pipetting robot on the Courses page (Surface & Colloid Science) |
| `.figure-crop--wide` | 5:4 window for long figures (`wide: true`): the 4:3 page drawn 1.45× the window width and shifted, trimming its empty margins on all sides | Home page SAXS instrument, under the group photo |

## 4. Images

### Shape rules

Images in the same place must have the same proportions:

| Where | Ratio | Typical size | How it's shown |
| --- | --- | --- | --- |
| Research areas, "In the Lab" strip, Research page banners | **2.2 : 1** | 1000–1320 × 455–600 px | Whole, full column width (`.research-image`) |
| People headshots | **1 : 1** | 800 × 800 px | `.person-photo` |
| Course photos | **3 : 4** (upright) | ≤600 px wide | Row of equal tiles under each course (`.course-photo`) |
| News thumbnails (lists) | 1 : 1 | any | Cropped to square by CSS (`.news-thumb`) |
| News story galleries | **4 : 3 frame** | ≤1600 px long side | Whole image inside the frame (`.gallery-frame`) |
| News story top photo | natural | ≤1600 px long side | Whole, max 600 px tall |
| Home group photo | ~2 : 1 | 1600 px wide | Whole |
| Contact portrait | 4 : 5 | 900 × 1125 px | Whole |
| Science Jubilee video poster | 1 : 1 | matches the square video | Video poster |

`_scripts/check_site.py` reports any research, lab, people or course image off its ratio.

### Cropping policy

- **Crop as little as possible.** Pick the ratio most images in the group already have. Anchor the crop on the subject, not the center, when needed: the Jubilee poster is anchored at 42% so the colored vials stay in, and the rooftop photo is anchored high to keep the person's head.
- **Combine instead of cropping** when photos have awkward shapes. Two upright photos side by side make one 2.2:1 banner (`hurricane-maria-team.jpg`), and many lab images are two-photo composites in the same style.
- **Pad instead of cropping** figures with white backgrounds. Adding white side margins brings them to the target ratio invisibly (`ultrasound.jpg` was 1.9:1 and was padded to 2.2:1).
- **Repeating patterns can take bigger crops:** the gold well plate keeps 3 of 6 rows. Faces, text, figure labels and flyers cannot.
- **Keep the uncropped original** in `_image_sources/`, mirroring the `assets/img/` path (e.g. `_image_sources/research/emulsions-original.png`).
- **Preview before applying:** draw the proposed crop boxes on a contact sheet and look at them before saving.

### File rules

- **Names:** lowercase, words separated by hyphens, `.jpg` (PNG only when transparency must be kept), e.g. `assets/img/people/firstname-lastname.jpg`, `assets/img/news/<slug>/01.jpg`. **Capitalization must match exactly.** macOS ignores case but GitHub Pages doesn't, so `Kevin-lee.jpg` works locally and breaks online. Fix case-only renames via a temporary name or `git mv`.
- **Formats:** web downloads are often AVIF or WebP with a `.png`/`.jpg` extension. Check with `file <name>` and convert (`sips -s format jpeg …` or Pillow).
- **Size:** at most 1600 px on the long side, about 1 MB or less, JPEG quality 85–88. Never upscale (`sips -Z` enlarges small images). Small sources (under ~600 px) look soft; ask the owner for a larger version.
- **Video:** compress (macOS: `avconvert -p PresetAppleM4V480pSD`) or embed from YouTube. GitHub rejects files over 100 MB.
- **Alt text:** describe what the image shows. Name only people the source identifies.
- **Interactive figures:** self-contained HTML pages (no outside files or network calls) in `assets/interactive/`, lowercase-hyphen names (e.g. `pipetting-robot.html`), with no Jekyll header so they're published untouched. Use the figure's "web version" (no labels or buttons, white background, sized for a 4:3 frame), embed it via `home_figures` in `_data/settings.yml`, and give it a `title` that describes it for screen readers. It currently has no visible caption, at the owner's request. Before publishing a new one, read the whole file and check it has no `fetch`, storage, cookies, `eval`, or `window.parent`/`top` access. The frame is sandboxed (scripts only). Interactive figures made with the Colorfigures skill come in two builds: a web version for embedding (`<name>.html`: no controls or labels, 4:3, looping demo) and a full one (`<name>-interactive.html`); their editable sources and rebuild steps live in `_image_sources/interactive/<name>/` (e.g. the SAXS instrument). On phones it must use `touch-action: pan-y` so a vertical swipe still scrolls the page.
- **Placeholders:** purple-striped labeled images generated with Pillow (camera icon, slot name, path, size). None are in use; use the same style if a new slot needs one.

## 5. Writing and content style

### General

- **Voice:** clear, factual, warm. Third person for people; "the group" / "our team" for the lab. No marketing superlatives beyond what a source says.
- **Names:**
  - Full name on first mention, first name after ("Brenden Pelkie… Brenden"). A known nickname goes in parentheses once: "Zachery (Zach) Wylie".
  - Prof. Pozzo is "Lilo D. Pozzo" or "Prof. Pozzo". Her legal name changed in 2013 from D.C. Pozzo to L.D. Pozzo. Both forms (and "L. Pozzo") appear in author lists and are bolded automatically.
- **Pronouns:** use the ones the source uses (e.g. Prof. Pozzo's post refers to Karen Li as "she"). If no source gives them, write around them with the person's name, or use they/them.
- **Dates:** "May 30th, 2025" or "August 7, 2026" in text; ISO dates (`2026-08-07`) in filenames and data.
- **Never invent facts:** dates, titles, positions, graduation years, pronouns, course descriptions. Leave them out, ask, and flag any assumption to the owner.

### News stories

- **First paragraph** works alone as the summary on the news lists: who, what, when.
- **Photos:** the best group photo is `image`; extra photos go in `gallery` with short captions.
- **Defense stories** follow this structure:
  1. Front matter: `title: "Congratulations, Dr. Surname!"`, `thumbnail: /assets/img/news/defense.jpg`, photos.
  2. "<Name> successfully defended <a> dissertation, titled "<Title>," on <date>, at/in <location>. … now holds a PhD in <field>." Add the advisor(s) or "Nth PhD student to graduate from the Pozzo group" when the source says so.
  3. The research in plain language, then a link to the dissertation in ResearchWorks, with any access restriction ("full text restricted to UW users until 2028"), then links to the person's papers.
  4. The abstract, verbatim from the announcement, in a collapsible `<details class="mb-4" markdown="1">` block with `<summary>Read the dissertation abstract</summary>` (template in CLAUDE.md).
  5. Collaborations, mentoring, celebrations (the hoodie ceremony) as the source describes them.
  6. "Congratulations, Dr. Surname!" and a "Connect with <first name>:" line, with links separated by ` · `.
- **Candidacy exams** use `/assets/img/news/candidacy.jpg` as the thumbnail.
- **After a defense:** move the person to `alumni` in `_data/people.yml` (no `image`; delete the headshot) with "(Ph.D. YEAR)".

### People

- `research` is one line in sentence case.
- `now:` holds verified current positions only; "Incoming …" for positions not yet started.
- Spell names as the person does on official documents; e.g. "Huat Thart Chiang", surname Chiang.

### Courses

- Name, a one-sentence description, and optional 3:4 photo tiles. An unknown description stays `''` (empty) until the owner provides it.

### Publications

- Newest first, numbered consecutively (newest = highest number).
- Authors as initials then surname (`H.T. Chiang, L.D. Pozzo`); journal as `Journal, vol(issue), pages (year)`; `url` = `https://doi.org/<doi>`.
- Only peer-reviewed journal articles (plus the existing SPIE proceedings entry); no abstracts, patents, theses or preprints.
- **Featured on the home page = the six newest papers with `corresponding: true`.** This is automatic: mark each paper where Prof. Pozzo is a corresponding author, and `_includes/publications.html` picks the newest six. Don't hand-pick papers or add `featured` flags. How to decide is in §6.
- **Open Access badge (`open_access: true`):** only if the journal is fully (gold) open access in the [DOAJ](https://doaj.org) **and** the paper's year is on or after the journal's DOAJ `oa_start` year. Currently qualifying: Digital Discovery (2022+), ACS "Au" journals (e.g. ACS Polymers Au, 2021+), npj Computational Materials, Nature Communications, Photoacoustics (2013+), Ultrasonics Sonochemistry (2021+), Journal of Open Hardware, Journal of Open Source Software. Not Advanced Materials Interfaces before 2023, and never hybrid journals.

## 6. Sources and verification

| What | Where to get it | How to verify / notes |
| --- | --- | --- |
| Publication metadata | Crossref `api.crossref.org/works/<doi>`; Google Scholar profile for discovering new papers | Title must match and Pozzo must be an author. In Oct 2026, 59 of 120 DOIs were wrong (dead or pointing to unrelated papers). Scholar truncates author lists and misattributes some papers. Crossref rate-limits parallel requests, so query one at a time with short pauses. |
| Corresponding author | Publisher page/PDF (asterisk or envelope), or OpenAlex `api.openalex.org/works/doi:<doi>` → `authorships[].is_corresponding` | Last author is *not* proof. RSC, ACS and IUCr pages block scripts (Cloudflare). Checked for #91 and newer. |
| Open access status | DOAJ `doaj.org/api/search/journals/issn:<ISSN>` → `oa_start` | ISSN from Crossref |
| Dissertations | UW ResearchWorks: `digital.lib.washington.edu/server/api/discover/search/objects?query=<surname>` | Confirm author and advisor; link the `https://hdl.handle.net/1773/…` handle; read `dc.embargo.terms` for access limits. Deposits appear 1–4 months after the defense (5 weeks for Wylie/Benstead, 4 months for Li). |
| Defense details and abstracts | The department's "Ph.D. Defense Announcement" PDF (owner provides) | Gives the title, date, room and abstract; quote abstracts verbatim |
| LinkedIn posts | **Ask the owner for the direct link** | Profiles and activity pages block scripts (HTTP 999 or a login wall), and search engines don't index posts, so posts can't be found by searching. A direct `linkedin.com/feed/update/urn:li:activity:<id>` link loads publicly; post date = `(id >> 22) / 1000` Unix seconds. Photos are at `media.licdn.com/…/feedshare-…`, sometimes only at 800 px. |
| Bluesky posts | Prof. Pozzo is `lilopozzo.bsky.social`; `public.api.bsky.app/xrpc/app.bsky.feed.getAuthorFeed?actor=…` | The account's feed is public (search needs a login). Full-size photos are under `embed.images[].fullsize`. |
| Positions, titles, awards | Prof. Pozzo's CV (`Pozzo_long_CV2025.pdf`, not published) or the owner | Don't rely on search-engine snippets about people's jobs; they can be out of date or wrong. |

## 7. Markdown and Jekyll pitfalls

- **No ` | ` in story or page text.** Kramdown turns any line containing a pipe into a table, which merges the links ("LinkedIn | ORCID" became "LinkedInORCID"). Separate links with ` · `.
- **HTML blocks with Markdown inside** need `markdown="1"` on the outer tag (e.g. `<details markdown="1">`, `<div class="col-md-7" markdown="1">`), with blank lines around the Markdown.
- **Internal links in layouts/includes** use `{{ '/path/' | relative_url }}`. Posts may use plain `/path/`.
- **Front matter:** quote strings containing `:` or `"`; keep the `---` lines intact. A YAML error stops the whole site from building.
- **Case sensitivity:** see §4. The local Mac build won't catch it, but `check_site.py` does.
- **Special characters** (ʻokina, macrons, subscripts like Sb₂S₃) are fine in UTF-8 files; don't replace them with HTML entities.

## 8. Checking and publishing

1. **Build locally:** the Mac's system Ruby (2.6) is too old for the current gems, so the build uses a separate pinned Gemfile outside the repo (details in CLAUDE.md, "Building locally").
2. **Run the check:** `python3 _scripts/check_site.py <built _site>`. It flags broken internal links (case-sensitive), off-ratio images and files over 1 MB, and exits with an error on broken links. Also check new outside links resolve (`curl -s -o /dev/null -w '%{http_code}' <url>`, expect 200/30x).
3. **Look at it:** screenshot the changed pages at 1280 px and ~520 px wide (headless Chrome can't go narrower than ~500 px). Confirm the menu stays on one line and nothing renders as a table or shows raw Markdown.
4. **Stage, report, and ask** before committing or pushing. Pushing to `main` publishes within a minute or two.
5. **After a push:** `gh run list` shows the Pages deploy. Live files are cached for up to 10 minutes; a hard refresh (Cmd+Shift+R) shows changes sooner.

**When a push or deploy fails**, check [githubstatus.com](https://www.githubstatus.com) first. GitHub had incidents on Oct 5, 6 and 7, 2026.

| Symptom | Meaning | Fix |
| --- | --- | --- |
| Push: `remote rejected … (Internal Server Error)` | GitHub server fault | Wait for the incident to clear, then push again |
| Push/fetch: `Could not resolve host: github.com` | Local network drop | Retry when online |
| Deploy: `job was not acquired by Runner` | GitHub Actions outage | `gh run rerun <id>` or push again |
| GitHub Desktop errors | Details are in `~/Library/Application Support/GitHub Desktop/logs/<date>.desktop.production.log` | Read the log before guessing |

## 9. Open items (awaiting the site owner)

Remove each item once it's resolved.

- **Corresponding author for #111 and #108** (Pozzo is last author; no data in OpenAlex), and confirmation for #110 (OpenAlex flags Pozzo; Holmberg is last author).
- **Community Service Design course:** exact title and a one-line description.
- **Older defense stories** (Pelkie, Guio, Politi, Scheiwiller, Lachowski) have no dissertation links. They're likely in ResearchWorks. Brenden Pelkie's archived title reads "Automation and Autonomous Experimentation for Sol-Gel Nanomaterial Synthesis", while the story says "Automated and Autonomous Experiments…".
- **Low-resolution images worth replacing:** `research/emulsions.jpg` (368 px source), `research/ultrasound.jpg` (342 px source), Claire Benstead's group selfie and Karen Li's hooding photo (800 px from LinkedIn).
- **Unplaced figures** from the old site: "AI Sampling", "DynamicLandscape" (possibly animated) and "Paella"; the originals are needed.

## 10. Decisions on record

- **Oct 2026:** rebuilt from the Wix site (pozzorg.com) on the academic theme; old news stories and images carried over; domain moved to GitHub Pages.
- Twitter/X removed entirely at the owner's request; `jekyll-seo-tag` replaced by `_includes/seo.html` (Open Graph tags only).
- Image proportions standardized: research/lab 2.2:1 (full column width), headshots 1:1, course photos 3:4; news galleries use uncropped 4:3 frames.
- Publication list audited against Crossref (59 links corrected); Open Access badges follow DOAJ; featured publications follow corresponding authorship.
- Defense stories include the dissertation link and the abstract in a collapsible block.
- **Oct 30, 2026:** interactive pipetting-robot figure (`assets/interactive/pipetting-robot.html`) added to the home page in a sandboxed frame, without a caption. At the owner's request it sits under the group photo at the photo's width; the photo column was widened (intro `col-md-5`, photo `col-md-7`) and the figure trimmed to a square window (`.figure-crop`) so the robot fills it (about 430 px tall at 1280 px).
- **Oct 30, 2026:** SAXS instrument figure (`assets/interactive/saxs-instrument.html`, drawn open with 90 cm collimation) added; `home_figure` became the list `home_figures`. At the owner's request the photo, robot and SAXS figure are stacked vertically at the photo's width; the SAXS figure uses a trimmed 5:4 window (`.figure-crop--wide`).
- **Oct 30, 2026:** at the owner's request the home page shows only the SAXS instrument under the group photo; the pipetting robot moved to the Courses page under Surface & Colloid Science (a course's optional `figure` in `_data/settings.yml`, square `.figure-crop` window, half the page width on desktop).
- The full CV PDF is intentionally not published (`*.pdf` is excluded from the build).
- Alumni are listed without photos.
