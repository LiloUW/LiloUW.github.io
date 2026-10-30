# SAXS instrument figure: sources

Interactive isometric figure of a SAXS/WAXS instrument (modelled on a Xenocs Xeuss 3.0), made with the
Colorfigures skill. Not published (folders starting with `_` are excluded by Jekyll).

| File | What it is |
| --- | --- |
| `saxs-instrument.src.html` | Full interactive figure: buttons, stats, see-through, labels |
| `saxs-instrument-web.src.html` | Web version, generated from the source above by `make_web.py` (do not edit by hand) |
| `make_web.py` | Regenerates the web source and rebuilds both published files |
| `core.js` | The Colorfigures engine both sources load while editing |

Published builds (single self-contained files):
- `assets/interactive/saxs-instrument-interactive.html` (from `saxs-instrument.src.html`)
- `assets/interactive/saxs-instrument.html` (from `saxs-instrument-web.src.html`; the one to embed)

Rebuild after editing `saxs-instrument.src.html` (from this folder): `python3 make_web.py`

The instrument is drawn open (no radiation-safety enclosure) on its base cabinet; slits S1 and S2 are 90 cm apart.

Testing hooks: `?sim=load:0,9;measure:1.6` freezes actions at given seconds for screenshots;
`?free=1&yaw=200&pitch=40` sets the view; `?xr=1&labels=1` opens the see-through with labels.
