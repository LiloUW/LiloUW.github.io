# Pozzo Research Group Website

Website for the Pozzo Research Group (Prof. Lilo D. Pozzo), Department of Chemical Engineering, University of Washington. Live at https://LiloUW.github.io.

## Built With

- [Jekyll](https://jekyllrb.com/), hosted on [GitHub Pages](https://pages.github.com/)
- The [academic](https://github.com/LeNPaul/academic) Jekyll theme by Paul Le (MIT License, see `THEME_LICENSE.txt`), with Bootstrap 5 and Font Awesome. The theme's layouts are copied into this repository and customized.

## Editing Content

Most content lives in YAML data files, so updates rarely require touching HTML:

| What | File |
| --- | --- |
| Menu, home/gallery images, courses, social links, contact info | `_data/settings.yml` |
| Research areas (Research page) | `_data/research.yml` |
| Group members and alumni (People page) | `_data/people.yml` |
| Publications (`featured: true` entries also appear on the home page) | `_data/publications.yml` |
| CV sections | `_data/cv/*.yml` (order set in `_data/cv/sections.yml`) |
| News stories (News page; newest three on the home page) | One Markdown file per story in `_posts/`; see [CLAUDE.md](CLAUDE.md) |
| Page intro text | `index.md`, `news.md`, `research.md`, `people.md`, `publications.md`, `courses.md`, `cv.md`, `contact.md` |

## Images

Images come from the old pozzorg.com site; a few placeholders remain. See [IMAGES_GUIDE.md](IMAGES_GUIDE.md) for every image slot. Original uploads go in `Images/`, which is git-ignored.

## Rules and Style

[SITE_GUIDE.md](SITE_GUIDE.md) records the site's visual style, image proportions, writing conventions, and how to check and publish changes. Read it before updating the site.

## Updating with Claude

[CLAUDE.md](CLAUDE.md) holds instructions that Claude Code reads automatically, including step-by-step instructions for adding news stories. In a Claude chat opened on this repository, asking for something like "add a news story about X with these photos" is enough.

## Local Development

1. Install Ruby 3.x and Bundler
2. Run `bundle install`
3. Run `bundle exec jekyll serve`
4. Visit `http://localhost:4000`

## Deployment

The site deploys automatically to GitHub Pages when changes are pushed to the `main` branch.

## License

Content © Lilo D. Pozzo. All rights reserved. Theme code © Paul Le, MIT License.
