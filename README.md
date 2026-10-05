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
| News/updates on the home page | Add a Markdown file to `_posts/` named `YYYY-MM-DD-title.md` |
| Page intro text | `index.md`, `research.md`, `people.md`, `publications.md`, `courses.md`, `cv.md`, `contact.md` |

## Images

All images are currently **placeholders**. See [IMAGES_GUIDE.md](IMAGES_GUIDE.md) for the list of files and how to replace them with laboratory photos.

## Local Development

1. Install Ruby 3.x and Bundler
2. Run `bundle install`
3. Run `bundle exec jekyll serve`
4. Visit `http://localhost:4000`

## Deployment

The site deploys automatically to GitHub Pages when changes are pushed to the `main` branch.

## License

Content © Lilo D. Pozzo. All rights reserved. Theme code © Paul Le, MIT License.
