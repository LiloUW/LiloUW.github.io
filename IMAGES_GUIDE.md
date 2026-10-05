# Site Images

Most images now come from the old pozzorg.com website. **Four slots still show labeled placeholders** (marked ⚠ below). To replace any image, save the new photo over that file using the same name, or change the matching `image:` path in the data file listed.

## Page images

Landscape photos, about **1200–1600 px** wide. Keep files under ~1 MB.

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
| `assets/img/research/science-jubilee.jpg` | Research: Science Jubilee spotlight (video poster) | `research.md` |
| `assets/video/jubilee-color-match-demo.mp4` | Research: Science Jubilee demo video (480p) | `research.md` |
| `assets/img/research/hurricane-maria-solar.png`, `pozzo-solar-installation.jpg` | Research: Hurricane Maria project | `research.md` |
| `assets/img/courses/kitchen-engineering.png` | Courses: Kitchen Engineering | `_data/settings.yml` (`courses`) |

Research and lab images are always shown whole (scaled, never cropped), so photos of similar shape look tidiest side by side. To add more, add another `- {image: ..., caption: ...}` line under `gallery` in `_data/settings.yml`.

## News images

Each story's images are in `assets/img/news/<story>/`. Shared thumbnails: `assets/img/news/defense.jpg` (defenses) and `assets/img/news/candidacy.jpg` (candidacy exams). See CLAUDE.md for how to add a story.

## Group member photos

Square headshots, at least **600 × 600 px**. Non-square photos are center-cropped automatically. Files are in `assets/img/people/`, named `firstname-lastname.jpg`:

- Real photos: `lilo-pozzo.jpg`, `abdul-moeez.jpg`, `hanson-chen.jpg`, `yu-fang-hsieh.jpg`. The last three came from the old site at only 168 × 206 px and look soft when enlarged; higher-resolution versions would help.
- ⚠ Placeholders: `kevin-lee.jpg`, `elena-toups.jpg`

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
