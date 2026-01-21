# Guide: Adding TOC Graphics to Publications

## What are TOC Graphics?

**TOC (Table of Contents) Graphics** are small visual summaries that appear alongside journal article abstracts. They provide a quick visual impression of the research without showing specific results. Most modern journal articles include these graphical abstracts.

## Current Status

The publications page (publications.md) is now set up with:
- ✅ Professional card-style layout with 150x150px TOC image placeholders
- ✅ Direct DOI links to all 18 most recent publications (2024-2025)
- ✅ Green "🔓 Open Access" badges for freely available articles
- ✅ Responsive design matching the students page
- ✅ UW purple color scheme (#4b2e83)
- ⏳ Awaiting TOC graphics to replace placeholders

---

## How to Find and Download TOC Graphics

### Option 1: Download from Journal Website (Recommended)

**This is the most reliable method for obtaining high-quality TOC graphics.**

#### Step-by-Step Instructions:

1. **Click on the article link** from the publications page (or visit the DOI link directly)

2. **Locate the TOC graphic** on the article page:
   - Nature journals: Usually displayed prominently near the abstract
   - ACS journals: Look for "Graphical Abstract" or "TOC Graphic"
   - RSC journals: Often shown as "Graphical Abstract"
   - Other publishers: Typically in the article header or abstract section

3. **Download the image**:
   - **Right-click** on the TOC graphic
   - Select **"Save image as..."**
   - Choose a descriptive filename (see naming convention below)

4. **Check image quality**:
   - Minimum size: 150x150 pixels (preferably larger)
   - Preferred format: JPG or PNG
   - File size: Keep under 500KB for fast loading

#### Naming Convention:

Use the publication number and first author's last name:
- Format: `pub-[NUMBER]-[LASTNAME].jpg`
- Examples:
  - `pub-112-vaddi.jpg` (Autonomous Phase Mapping...)
  - `pub-111-pelkie.jpg` (Accelerated sol-gel synthesis...)
  - `pub-110-wylie.jpg` (Synthesis, assembly, and electrochemical...)

### Option 2: Search on Publisher-Specific Repositories

Some publishers maintain repositories or allow searching by DOI:

1. **Nature Portfolio** (Nature, Nature Materials, npj journals):
   - Visit: https://www.nature.com/
   - Search by article DOI
   - TOC graphics are usually high-resolution

2. **ACS Publications** (Langmuir, Biomacromolecules, ACS Synthetic Biology):
   - Visit: https://pubs.acs.org/
   - Search by article title or DOI
   - Look for "Graphical Abstract"

3. **RSC Publishing** (Soft Matter, Digital Discovery, J. Mater. Chem. A):
   - Visit: https://www.rsc.org/
   - Search by DOI
   - Graphics often labeled as "Graphical Abstract"

### Option 3: Check ResearchGate or Author Repositories

If the journal website doesn't show the TOC graphic clearly:

1. Search for the article on **ResearchGate**: https://www.researchgate.net/
2. Many authors upload high-resolution versions of their TOC graphics
3. You may need to create a free account to download

### Option 4: Contact Co-Authors

For older publications where graphics are hard to find:
- Reach out to current or former students who were co-authors
- They likely have the original high-resolution files
- Use the LinkedIn profiles from the students page to contact them

---

## Image Specifications

**Recommended specifications for TOC graphics:**

| Property | Specification |
|----------|--------------|
| **Format** | JPG or PNG (JPG preferred for photos, PNG for diagrams) |
| **Dimensions** | Minimum 150x150px, preferably 300x300px or larger |
| **Aspect Ratio** | Square preferred, but 3:2 or 4:3 also acceptable |
| **File Size** | Keep under 500KB (compress if needed) |
| **Color** | Full color (as published in the journal) |
| **Resolution** | 72-150 DPI for web display |

**Image Optimization:**
- Use online tools like [TinyPNG](https://tinypng.com/) or [Squoosh](https://squoosh.app/) to compress images
- Maintain visual quality while reducing file size
- Square cropping works best for consistency

---

## Adding TOC Graphics to the Website

### Step 1: Save the Image

Save downloaded TOC graphics in:
```
assets/images/publications/
```

With the naming convention: `pub-[NUMBER]-[LASTNAME].jpg`

### Step 2: Update publications.md

Replace the placeholder:
```html
<div class="pub-placeholder">TOC Graphic</div>
```

With the actual image:
```html
<img src="/assets/images/publications/pub-112-vaddi.jpg" alt="Publication 112 TOC" class="pub-image">
```

### Step 3: Commit and Push to GitHub

```bash
# Navigate to your project directory
cd "/Users/dpozzo/Claude Code /Pozzo Website"

# Add the new images
git add assets/images/publications/

# Add the updated publications.md
git add publications.md

# Commit with a descriptive message
git commit -m "Add TOC graphics for publications [list numbers]"

# Push to GitHub
git push
```

---

## Example: Adding Publication #112 TOC Graphic

**Before:**
```html
<div class="pub-container">
<div class="pub-placeholder">TOC Graphic</div>
<div class="pub-content">
<div class="pub-title">112. Autonomous Phase Mapping of Gold Nanoparticles Synthesis</div>
...
</div>
</div>
```

**After:**
```html
<div class="pub-container">
<img src="/assets/images/publications/pub-112-vaddi.jpg" alt="Publication 112 TOC" class="pub-image">
<div class="pub-content">
<div class="pub-title">112. Autonomous Phase Mapping of Gold Nanoparticles Synthesis</div>
...
</div>
</div>
```

---

## Priority Publications for TOC Graphics

Start with the most recent and most cited publications:

### High Priority (2024-2025):
- ✅ **#112** - Autonomous Phase Mapping (npj Computational Materials) - [Link](https://doi.org/10.1038/s41524-025-01822-z)
- ✅ **#111** - Accelerated sol-gel synthesis (Digital Discovery) - [Link](https://doi.org/10.1039/D5DD00274E)
- ✅ **#110** - Ultrasmall Sb₂S₃ nanoparticles (J. Mater. Chem. A) - [Link](https://doi.org/10.1039/D5TA04184H)
- ✅ **#99** - Silver nanoplate formation (Digital Discovery) - [Link](https://doi.org/10.1039/D4DD00211C)
- ✅ **#98** - Interfacial dynamics (Nature Communications) - [Link](https://doi.org/10.1038/s41467-024-52136-6)

### Medium Priority (2021-2023):
Work backwards from 2023 publications, prioritizing highly cited articles and Open Access publications.

### Lower Priority (2004-2020):
Older publications can be added as time permits or as original files are located.

---

## Troubleshooting

**Problem: Can't find the TOC graphic on the journal website**
- Solution: Try searching on ResearchGate or contact the first author
- Some older journals didn't require TOC graphics

**Problem: Image is too large (>500KB)**
- Solution: Use [TinyPNG](https://tinypng.com/) to compress without losing quality
- Or resize to 300x300px using online tools

**Problem: Image has wrong aspect ratio**
- Solution: Crop to square using free tools like [Canva](https://www.canva.com/) or Preview (Mac)
- Or accept 3:2 ratio - the CSS will handle it

**Problem: Image is behind a paywall**
- Solution: For Open Access articles, the full article (including graphics) should be freely available
- For subscription articles, try ResearchGate or institutional access

**Problem: Multiple graphics available (graphical abstract vs. TOC)**
- Solution: Prefer the official "TOC Graphic" or "Graphical Abstract"
- Choose the one that best summarizes the paper visually

---

## Copyright and Fair Use

**Important considerations:**

✅ **You CAN use TOC graphics** from your own publications on your personal academic website - this is considered fair use for scholarly communication

✅ **Recommended practice**:
- You are the author/co-author on these publications
- Using your own research graphics for academic purposes is standard practice
- Many journals explicitly allow authors to reuse their graphics

✅ **Best practice**:
- Download directly from the publisher's website where possible
- This ensures you have the official, high-quality version
- No additional permissions needed for your own publications

---

## Quick Reference: Journal URLs

Here are direct links to major publishers for your articles:

| Publisher | URL | Notes |
|-----------|-----|-------|
| **Nature Portfolio** | https://www.nature.com/ | npj journals, Nature Communications, Nature Materials |
| **RSC Publishing** | https://www.rsc.org/ | Soft Matter, Digital Discovery, J. Mater. Chem. A |
| **ACS Publications** | https://pubs.acs.org/ | Langmuir, Biomacromolecules, ACS Synthetic Biology |
| **Elsevier** | https://www.sciencedirect.com/ | J. Colloid Interface Sci., Ultrasonics Sonochemistry |
| **Wiley** | https://onlinelibrary.wiley.com/ | Angewandte Chemie |
| **PNAS** | https://www.pnas.org/ | Proceedings of the National Academy of Sciences |
| **IUCr** | https://journals.iucr.org/ | J. Applied Crystallography |

---

## Progress Tracking

**Total Publications:** 114
**Publications with article links:** 18 (2024-2025)
**Publications with TOC placeholders:** 18
**TOC graphics added:** 0 (awaiting collection)

**Next Steps:**
1. Start with the 5 highest priority publications (#112, 111, 110, 99, 98)
2. Download and add their TOC graphics
3. Test the layout to ensure images display correctly
4. Continue with remaining 2024-2025 publications
5. Work backwards through earlier publications

---

## Getting Help

If you need assistance:
- Check the journal's "For Authors" or "Author Guidelines" page
- Contact the journal editorial office for image files
- Reach out to co-authors who may have the original files
- Use the LinkedIn profiles on the students page to contact former students

---

**Questions?** The publication page structure is ready - just add the images and watch your research come to life visually!

## Resources

- [JMIR Guide to TOC Images](https://support.jmir.org/hc/en-us/articles/115001261607-What-is-a-TOC-image-and-where-how-do-I-upload-it)
- [ACS TOC Graphics Guidelines](https://pubs.acs.org/pb-assets/acspubs/Migrated/cmatex_tocguide-1388359678000.pdf)
- [MIT Communication Lab: TOC Figures](https://mitcommlab.mit.edu/meche/2020/05/15/toc-figuresmore-than-just-a-thumbnail/)
