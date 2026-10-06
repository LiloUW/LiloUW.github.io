# Site Images

Most images now come from the old pozzorg.com website. **Two slots still show labeled placeholders** (marked ⚠ below). To replace any image, save the new photo over that file using the same name, or change the matching `image:` path in the data file listed.

## Page images

Research-area and lab images are **2.2 : 1 banners** (e.g. 1320 × 600 px); all other proportions are in SITE_GUIDE.md section 3. Keep files under ~1 MB. Uncropped originals of every cropped image are kept in `_image_sources/`.

| File | Where it appears | Configured in |
| --- | --- | --- |
| `assets/img/home.jpg` | Home page, group photo next to the introduction | `_data/settings.yml` (`home_image`) |
| `assets/img/lab/well-plate-synthesis.jpg` | Home page "In the Lab" strip | `_data/settings.yml` (`gallery`) |
| `assets/img/lab/vials-and-plate.jpg` | Home page "In the Lab" strip | `_data/settings.yml` (`gallery`) |
| `assets/img/lab/hydrogel-membranes.jpg` | Home page "In the Lab" strip | `_data/settings.yml` (`gallery`) |
| `assets/img/contact.jpg` | Contact page (portrait of Prof. Pozzo) | `_data/settings.yml` (`contacts`) |
| `assets/img/research/ai-discovery.jpg` | Research: AI-Driven Materials Discovery | `_data/research.yml` |
| `assets/img/research/energy-storage.jpg` | Research: Energy Storage Materials | `_data/research.yml` |
| `assets/img/research/emulsions.jpg` | ⚠ Research: Functional Emulsions (placeholder) | `_data/research.yml` |
| `assets/img/research/scattering.jpg` | Research: Neutron & X-ray Scattering | `_data/research.yml` |
| `assets/img/research/self-assembly.jpg` | Research: Self-Assembly & Nanostructures | `_data/research.yml` |
| `assets/img/research/ultrasound.jpg` | ⚠ Research: Ultrasound & Sonochemistry (placeholder) | `_data/research.yml` |
| `assets/img/research/science-jubilee.jpg` | Research: Science Jubilee spotlight (square video poster) | `research.md` |
| `assets/video/jubilee-color-match-demo.mp4` | Research: Science Jubilee demo video (480p) | `research.md` |
| `assets/img/research/hurricane-maria.jpg` | Research: Hurricane Maria project (two photos combined into one 2.2:1 banner) | `research.md` |
| `assets/img/courses/kitchen-engineering.png` | Courses: Kitchen Engineering | `_data/settings.yml` (`courses`) |

These images are displayed whole, so new ones should be cropped to 2.2 : 1 first. To add more, add another `- {image: ..., caption: ...}` line under `gallery` in `_data/settings.yml`.

## News images

Each story's images are in `assets/img/news/<story>/`. Shared thumbnails: `assets/img/news/defense.jpg` (defenses) and `assets/img/news/candidacy.jpg` (candidacy exams). See CLAUDE.md for how to add a story.

## Group member photos

Square headshots, at least **600 × 600 px**. Non-square photos are center-cropped automatically. Files are in `assets/img/people/`, named `firstname-lastname.jpg`:

All current members have real photos: `lilo-pozzo.jpg`, `kevin-lee.jpg`, `abdul-moeez.jpg`, `hanson-chen.jpg`, `yu-fang-hsieh.jpg`, `elena-toups.jpg`.

**Use exactly these lowercase names.** Macs ignore capitalization in file names but the live site does not, so `Kevin-lee.jpg` works on your computer and is a broken image online.

When someone joins the group, add their photo to this folder and an entry in `_data/people.yml`. Alumni are listed without photos.

## Publication TOC graphics (optional)

To show a table-of-contents graphic beside a publication, add the image to `assets/img/toc/` (e.g. `assets/img/toc/114.jpg`, about 400 px wide) and add an `image:` line to that entry in `_data/publications.yml`:

```yaml
- number: 114
  year: 2025
  title: "Assembly of small silica nanoparticles using lipid-tethered DNA ‘bonds’"
  ...
  image: "assets/img/toc/114.jpg"
```

## Tips

- Shrink large camera photos before uploading (macOS Preview: Tools → Adjust Size).
- Get permission from everyone who appears in a photo.
- After pushing, GitHub Pages takes a few minutes to update. Hard-refresh the browser (Cmd+Shift+R) if an old image still shows.
