# Replacing the Placeholder Images

Every image on the site is currently a labeled placeholder. Each placeholder shows its own file path, so to replace one, **save the real photo over that file using the same name** (JPG). No code changes are needed.

If you'd rather use a different file name or format (e.g. PNG), update the matching `image:` path in the data file listed below.

## Laboratory and page images

Landscape photos, about **1200 × 800 px** (3:2). Keep files under ~500 KB.

| File | Where it appears | Configured in |
| --- | --- | --- |
| `assets/img/home.jpg` | Home page, next to the introduction | `_data/settings.yml` (`home_image`) |
| `assets/img/lab/lab-1.jpg` | Home page "In the Lab": laboratory automation platform | `_data/settings.yml` (`gallery`) |
| `assets/img/lab/lab-2.jpg` | Home page "In the Lab": high-throughput SAXS instrument | `_data/settings.yml` (`gallery`) |
| `assets/img/lab/lab-3.jpg` | Home page "In the Lab": nanomaterials synthesis | `_data/settings.yml` (`gallery`) |
| `assets/img/contact.jpg` | Contact page | `_data/settings.yml` (`contacts`) |
| `assets/img/research/ai-discovery.jpg` | Research page: AI-Driven Materials Discovery | `_data/research.yml` |
| `assets/img/research/energy-storage.jpg` | Research page: Energy Storage Materials | `_data/research.yml` |
| `assets/img/research/emulsions.jpg` | Research page: Functional Emulsions | `_data/research.yml` |
| `assets/img/research/scattering.jpg` | Research page: Neutron & X-ray Scattering | `_data/research.yml` |
| `assets/img/research/self-assembly.jpg` | Research page: Self-Assembly & Nanostructures | `_data/research.yml` |
| `assets/img/research/ultrasound.jpg` | Research page: Ultrasound & Sonochemistry | `_data/research.yml` |

Gallery captions can be edited in `_data/settings.yml`. To add more gallery photos, add another `- {image: ..., caption: ...}` line there.

## Group member photos

Square headshots, at least **600 × 600 px**. Non-square photos are center-cropped automatically.

Files are in `assets/img/people/`, named `firstname-lastname.jpg`:

`lilo-pozzo.jpg`, `kevin-lee.jpg`, `claire-benstead.jpg`, `abdul-moeez.jpg`, `zachery-wylie.jpg`, `hanson-chen.jpg`, `yu-fang-hsieh.jpg`, `elena-toups.jpg`, `tobias-rangel.jpg`

When someone joins the group, add their photo to this folder and an entry in `_data/people.yml`. Alumni are listed without photos.

## Publication TOC graphics (optional)

To show a table-of-contents graphic beside a publication, add the image to `assets/img/toc/` (e.g. `assets/img/toc/114.jpg`, about 400 px wide) and add an `image:` line to that entry in `_data/publications.yml`:

```yaml
- number: 114
  year: 2025
  title: "Programmable Conformational Switching in Peptoid Nanosheets via pH and Light"
  ...
  image: "assets/img/toc/114.jpg"
```

## Tips

- Shrink large camera photos before uploading (macOS Preview: Tools → Adjust Size).
- Get permission from everyone who appears in a photo.
- After pushing, GitHub Pages takes a few minutes to update. Hard-refresh the browser (Cmd+Shift+R) if the old placeholder still shows.
