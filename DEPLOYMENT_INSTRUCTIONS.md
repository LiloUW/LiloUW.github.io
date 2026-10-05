# Deployment Instructions for GitHub Pages

## Step 1: Create GitHub Repository

1. Go to [GitHub](https://github.com) and log in with the account **LiloUW**
2. Click the "+" icon in the top right and select "New repository"
3. Name the repository: **LiloUW.github.io** (this must be the exact name for a user site)
4. Set the repository to **Public**
5. Do NOT initialize with README, .gitignore, or license (we already have these)
6. Click "Create repository"

## Step 2: Push Your Local Repository to GitHub

After creating the repository on GitHub, run these commands in your terminal:

```bash
# Navigate to your project directory (if not already there)
cd ~/Documents/GitHub/LiloUW.github.io

# Set your default branch to main (recommended)
git branch -M main

# Add the GitHub repository as remote origin
git remote add origin https://github.com/LiloUW/LiloUW.github.io.git

# Push your code to GitHub
git push -u origin main
```

You may be prompted to log in to GitHub. Use your GitHub credentials.

## Step 3: Enable GitHub Pages

1. Go to your repository on GitHub: https://github.com/LiloUW/LiloUW.github.io
2. Click on "Settings" (gear icon) in the top menu
3. In the left sidebar, click "Pages" under "Code and automation"
4. Under "Build and deployment":
   - Source: Select "Deploy from a branch"
   - Branch: Select "main" and folder "/ (root)"
   - Click "Save"

## Step 4: Wait for Deployment

GitHub Pages will automatically build and deploy your site. This may take a few minutes.

- You can check the deployment status in the "Actions" tab of your repository
- Once complete, your site will be live at: **https://LiloUW.github.io**

## Step 5: Verify Your Website

1. Visit https://LiloUW.github.io in your browser
2. Check that all pages are working:
   - Home, Research, People, Publications, Courses, CV, and Contact pages

## Updating Your Website

To make changes to your website in the future:

1. Edit the files locally
2. Commit your changes:
   ```bash
   git add .
   git commit -m "Description of your changes"
   ```
3. Push to GitHub:
   ```bash
   git push
   ```
4. GitHub Pages will automatically rebuild and deploy your site

## Customization Tips

### Replacing Placeholder Images

Save real photos over the placeholder files using the same names. See `IMAGES_GUIDE.md` for the full list.

### Updating Content

Most content is stored in data files under `_data/` (people, publications, research areas, CV, contact info). See the "Editing Content" table in `README.md`.

### Changing the Appearance

Colors and fonts are set in `_sass/main.scss`. Page layouts are in `_layouts/` and `_includes/` (from the [academic](https://github.com/LeNPaul/academic) theme).

## Troubleshooting

**Site not updating after push:**
- Check the Actions tab for build errors
- Ensure your changes were actually pushed: `git status` should show "nothing to commit, working tree clean"

**404 errors:**
- Verify the repository name is exactly **LiloUW.github.io**
- Check that GitHub Pages is enabled in Settings > Pages

**Theme not rendering correctly:**
- Make sure the Gemfile is committed and pushed
- GitHub Pages may take 5-10 minutes to rebuild after changes

## Testing Locally (Optional)

To preview your site locally before pushing:

```bash
# Install dependencies (first time only)
bundle install

# Run the local server
bundle exec jekyll serve

# Visit http://localhost:4000 in your browser
```

## Support

- [GitHub Pages Documentation](https://docs.github.com/en/pages)
- [Jekyll Documentation](https://jekyllrb.com/docs/)
- [academic Jekyll theme](https://github.com/LeNPaul/academic)

---

**Note:** If you encounter any issues or need to make significant changes, feel free to reach out for assistance!
