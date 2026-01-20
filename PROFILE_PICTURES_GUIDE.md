# Guide: Adding Student Profile Pictures

## LinkedIn Profiles Found

I've successfully searched for and found LinkedIn profiles for many of your current and former students. Here's a summary:

### Current Students & Postdocs (4/8)
✅ **Kevin Lee** - [LinkedIn](https://www.linkedin.com/in/kevin-lee-312317b4/)
✅ **Claire Benstead** - [LinkedIn](https://www.linkedin.com/in/claire-benstead-464b70178/)
✅ **Abdul Moeez** - [LinkedIn](https://www.linkedin.com/in/abdul-moeez-90b960b6)
✅ **Zachery Wylie** - [LinkedIn](https://www.linkedin.com/in/zach-wylie-09299116b/)
❌ Hanson Chen - Not found
❌ Elena Toups - Not found
❌ Tobias Rangel - Not found
❌ Yu-Fang Hsieh - Not found

### Past Postdocs (3/6)
✅ **Shayna Hilburg** - [LinkedIn](https://www.linkedin.com/in/shaynahilburg/)
✅ **Greg Newbloom** - [LinkedIn](https://www.linkedin.com/in/greg-newbloom-ab125458/)
✅ **Fabio Baum** - [LinkedIn](https://linkedin.com/in/fábio-baum)
❌ David Li - Not found
❌ Kiran Vaddi - Not found
❌ Rebecca Vincent - Not found

### Past PhD Students (11/15)
✅ **Kacper Lachowski** - [LinkedIn](https://www.linkedin.com/in/klachowski/)
✅ **Maria Politi** - [LinkedIn](https://www.linkedin.com/in/maria-politi-97a631170/)
✅ **Lorenzo Guio** - [LinkedIn](https://www.linkedin.com/in/lorenzoguio/)
✅ **Sage Scheiwiller** - [LinkedIn](https://www.linkedin.com/in/sage-scheiwiller-8b9160105)
✅ **Jaime Rodriguez** - [LinkedIn](https://www.linkedin.com/in/jaimerodriguez26/)
✅ **Yi-Ting Lee** - [LinkedIn](https://www.linkedin.com/in/yi-ting-lee-2267135b/)
✅ **Yuyin Xi** - [LinkedIn](https://www.linkedin.com/in/yuyin-xi-03339b3b/)
✅ **Jeff Richards** - [LinkedIn](https://www.linkedin.com/in/jeffrey-richards-90617512/)
✅ **Kjersta Larson-Smith** - [LinkedIn](https://www.linkedin.com/in/kjersta-larson-smith-54a85640)
✅ **Kathleen Weigandt** - At NIST (no LinkedIn found)
✅ **Caitlyn Wolf** - At NIST (no LinkedIn found)
❌ Huat Thart-Chiang - Not found
❌ Ryan Kastilani - Not found
❌ Pablo de la Iglesia - Not found
❌ Monica Ospinal - Not found

**Total: 18 LinkedIn profiles found out of ~35 students searched**

---

## How to Add Profile Pictures

### Option 1: Download from LinkedIn Manually (Recommended)

**Important Note:** While it's technically possible to view LinkedIn profile pictures, you should obtain permission before using them. The best approach is:

1. **Contact each student/postdoc** via email and ask:
   - If they'd like to be featured on the website
   - If they can provide a professional photo (preferably square, 300x300px minimum)
   - If they're comfortable with you using their LinkedIn photo

2. **For those who agree:**
   - Ask them to send you their photo directly
   - Or they can download their own LinkedIn photo:
     - Go to their LinkedIn profile
     - Click on their profile picture
     - Right-click and "Save image as..."

3. **Save the photos** in the `assets/images/students/` folder with the naming convention:
   - `firstname-lastname.jpg` (e.g., `shayna-hilburg.jpg`)

4. **Update students.md** by replacing:
   ```html
   <div class="student-placeholder">Photo</div>
   ```
   with:
   ```html
   <img src="/assets/images/students/firstname-lastname.jpg" alt="Student Name" class="student-image">
   ```

### Option 2: Email Template for Students

Here's a template email you can send to students:

```
Subject: Website Profile - Pozzo Research Group

Dear [Student Name],

I'm updating our research group website (https://LiloUW.github.io) and would like to feature you on our students page with your LinkedIn profile link.

Would you be willing to:
1. Provide a professional headshot photo (square format, at least 300x300 pixels)?
2. Verify your LinkedIn profile URL is correct: [INSERT LINK]

You can send the photo to dpozzo@uw.edu or submit it via GitHub if you're comfortable with that.

Thank you!

Best regards,
Lilo Pozzo
```

### Option 3: Students Can Add Their Own Photos (via GitHub)

For students familiar with GitHub:

1. Fork the repository
2. Add their photo to `assets/images/students/firstname-lastname.jpg`
3. Edit `students.md` to replace their placeholder with:
   ```html
   <img src="/assets/images/students/firstname-lastname.jpg" alt="Your Name" class="student-image">
   ```
4. Submit a pull request

---

## Photo Guidelines

**Recommended specifications:**
- **Format:** JPG or PNG
- **Size:** At least 300x300 pixels (square)
- **File size:** Keep under 200KB for fast loading
- **Style:** Professional headshot, preferably against a solid background
- **Naming:** `firstname-lastname.jpg` (all lowercase, hyphen between names)

**Example filenames:**
- `shayna-hilburg.jpg`
- `kacper-lachowski.jpg`
- `maria-politi.jpg`

---

## Current Website Status

The student page is now set up with:
- ✅ Professional card-style layout with circular photo placeholders
- ✅ LinkedIn profile links (where found)
- ✅ Current positions and research focus
- ✅ Responsive design that works on mobile and desktop
- ✅ UW purple color scheme (#4b2e83)
- ⏳ Awaiting profile photos from students

---

## Privacy & Permissions

**Important considerations:**
- Always ask permission before using someone's photo
- LinkedIn's terms of service discourage automated scraping of profile pictures
- Some students may prefer not to have their photo displayed
- Respect GDPR/privacy concerns, especially for international students

---

## Next Steps

1. Review the list of found LinkedIn profiles
2. Decide which students to contact for photos
3. Send out email requests (use template above)
4. As photos come in, add them to `assets/images/students/`
5. Update `students.md` to replace placeholders with actual images
6. Commit and push changes to GitHub

---

**Questions?** All the LinkedIn profiles are already linked on the website. The photo placeholders are styled to look professional even before real photos are added!
