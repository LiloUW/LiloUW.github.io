# Pozzo Research Group Website

Website of the Pozzo Research Group (Prof. Lilo D. Pozzo), Department of Chemical Engineering, University of Washington. Live at **https://pozzorg.com** (also https://LiloUW.github.io).

It is a [Jekyll](https://jekyllrb.com/) site hosted on [GitHub Pages](https://pages.github.com/): pushing to the `main` branch publishes it within a minute or two. The design is adapted from the [academic](https://github.com/LeNPaul/academic) Jekyll theme by Paul Le (MIT License, see `THEME_LICENSE.txt`), with Bootstrap 5 and Font Awesome.

## Where things are

Most updates only touch a data file or a Markdown file; HTML templates rarely need to change.

```
_pages/          the pages: index.md (home), research, people, publications, courses, cv, contact, news
_posts/          news stories, one Markdown file each (YYYY-MM-DD-slug.md)
_data/           the content in YAML
  settings.yml     menu, home photo and figures, "In the Lab" strip, courses, footer icons, contact card
  people.yml       group members and alumni
  publications.yml publications (the six newest with Prof. Pozzo as corresponding author are featured)
  research.yml     research areas
  cv/              CV sections
assets/          files served as-is: img/, interactive/ (animated figures), video/, css/, libs/
_layouts/        page templates          _includes/  shared pieces (header, footer, ...)
_sass/main.scss  colours and styles
_sources/        originals, not published: uncropped images, figure source code, the CV PDF
_scripts/        build.sh (local build + checks), check_site.py
docs/            the guides listed below
_config.yml      site title, description and build settings     CNAME  the custom domain
```

## Guides

| Guide | Read it for |
| --- | --- |
| [docs/HOW_TO.md](docs/HOW_TO.md) | Step-by-step recipes: add a news story, a person, a publication; change courses, research areas, the CV, the menu, figures |
| [docs/SITE_GUIDE.md](docs/SITE_GUIDE.md) | The rules: the owner's standing rules, visual style, image proportions, writing conventions, fact checking, publishing |
| [docs/IMAGES_GUIDE.md](docs/IMAGES_GUIDE.md) | Every image on the site, its file and where it's configured |
| [docs/DEPLOYMENT.md](docs/DEPLOYMENT.md) | Hosting, the pozzorg.com domain, building locally, troubleshooting |
| [CLAUDE.md](CLAUDE.md) / [AGENTS.md](AGENTS.md) | Instructions for AI agents (Claude Code loads CLAUDE.md automatically) |

## Quick start

1. Edit the relevant file (see [docs/HOW_TO.md](docs/HOW_TO.md)).
2. Preview and check: `_scripts/build.sh`, then `python3 -m http.server 8000 -d /tmp/pozzo-site` and open http://localhost:8000.
3. Commit and push to `main`.

With Claude Code opened on this folder, asking something like "add a news story about X with these photos" is enough; it follows CLAUDE.md and the guides.

## License

Content © Lilo D. Pozzo. All rights reserved. Theme code © Paul Le, MIT License.
