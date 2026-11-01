# Sources (not published)

Originals and source files behind what the site shows. Jekyll skips folders starting with `_`, so nothing here
is published; the site only uses the processed copies in `assets/`.

| Folder | Holds |
| --- | --- |
| `images/` | Uncropped or full-size originals of images that were cropped, padded or combined for the site. Mirrors `assets/img/` (e.g. `images/research/emulsions-original.png` → `assets/img/research/emulsions.jpg`). Keep the original here whenever you crop a new image. |
| `interactive/<name>/` | Source code of an interactive figure and how to rebuild it (each has a README). The built, self-contained pages are in `assets/interactive/`. |
| `documents/` | Reference documents used to check facts, e.g. Prof. Pozzo's full CV (`Pozzo_long_CV2025.pdf`, intentionally not published). |

Raw uploads waiting to be processed go in `Images/` at the repository root instead (git-ignored).
