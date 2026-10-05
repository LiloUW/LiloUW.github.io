# Pozzo Research Group website

Jekyll site served by GitHub Pages from `main` (https://LiloUW.github.io). Layouts are adapted from the "academic" theme by Paul Le and live in `_layouts/` and `_includes/`. Most content is in YAML under `_data/`; see README.md for the full map.

## Adding a news story

Each story is one Markdown file in `_posts/`, named `YYYY-MM-DD-short-slug.md` (lowercase, hyphens). The date in the filename is the publication date. Stories appear newest first on `/news/`, and the three newest also appear on the home page.

1. **Images.** Put them in `assets/img/news/<short-slug>/` as `01.jpg`, `02.jpg`, … Convert and resize first, because uploads are often AVIF/HEIC/PNG files with misleading extensions and full camera resolution:
   ```bash
   sips -s format jpeg -s formatOptions 85 -Z 1600 "<source image>" --out assets/img/news/<short-slug>/01.jpg
   ```
   `-Z 1600` sets the longest side to 1600 px, and sips will also *enlarge* smaller images, so first check the size with `sips -g pixelWidth -g pixelHeight <file>` and drop `-Z 1600` if the image is already smaller. Check with `file` that the result is real JPEG data.
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
4. **Related updates.** A defense usually also means moving the person from `current` to `alumni` in `_data/people.yml` (alumni have no `image`; delete their headshot in `assets/img/people/`). A new paper goes in `_data/publications.yml`.
5. **Verify.** Run a local build if possible (see "Building locally" below) and check that every image path in the post exists.

Writing style used in existing posts: third person ("Brenden Pelkie successfully defended his dissertation, titled \"…\", on May 30th, 2025."), dissertation or talk titles in quotes, and a closing "Congratulations, Dr. X!" for defenses. People are referred to by first name after the first mention.

## Other common updates

- **People:** `_data/people.yml`. Current members need a square headshot at `assets/img/people/firstname-lastname.jpg` (at least 600 px; shrink larger photos with `sips -Z 800`).
- **Publications:** `_data/publications.yml`, newest first, `number` counting up. Set `featured: true` on the four newest so they show on the home page. Author format `H.T. Chiang, L.D. Pozzo`; journal format `Journal, vol(issue), pages (year)`; link through `https://doi.org/...`.
- **Images:** IMAGES_GUIDE.md lists every image slot and the ones that are still placeholders.

## Constraints

- GitHub rejects files over 100 MB, and the site should stay light. Keep images under ~1 MB and compress videos (macOS: `avconvert -p PresetAppleM4V480pSD`) or embed them from YouTube.
- `Images/` holds the original uploads. It is git-ignored and excluded from the build; never reference it from pages.
- Use `relative_url` for internal links in layouts and includes.
- File names must be lowercase with hyphens and match references exactly. macOS ignores case but GitHub Pages does not, so a case mismatch passes local checks and breaks online. Rename uploads (e.g. `Kevin-lee.jpg` → `kevin-lee.jpg`) via a temporary name or `git mv`, and check links case-sensitively.
- A failed GitHub Pages run with "job was not acquired by Runner" in the deploy step is a GitHub outage, not a site error: check with `gh run view <id>`, then `gh run rerun <id>` or push again.

## Building locally

The system Ruby on the main development Mac is 2.6, too old for the current `github-pages` gem. A working approach is a separate Gemfile pinning `github-pages` 227 (with `ffi < 1.17`, `nokogiri < 1.14`, `public_suffix < 5`, `activesupport < 7`, `zeitwerk < 2.7`, `concurrent-ruby < 1.3.5`, `webrick`) installed outside the repo, then:
```bash
LANG=en_US.UTF-8 BUNDLE_GEMFILE=<that Gemfile> bundle exec jekyll build -d <scratch dir>/_site
```
