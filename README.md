# The Attic Website

This is the static website for The Attic, deployed on Cloudflare Workers.

## Live Site
- URL: https://theattic.nikvalentine.workers.dev
- Custom Domain (optional): Can be added in Cloudflare dashboard

## Project Structure
theattic-website/
- index.html          # Homepage
- about.html          # About page
- contact.html        # Contact page
- project-5.html      # Project page
- new-gallery-5.html  # Gallery page
- content/           # Images and media
- static/            # CSS files
- universal/         # JavaScript files
- workers-site/      # Cloudflare Worker code
- wrangler.toml      # Cloudflare configuration

## Making Changes

### 1. Clone the repository (first time only)
git clone https://github.com/nooodle/theattic-website.git
cd theattic-website

### 2. Make your changes
- Edit HTML files directly
- Add new images to appropriate folders
- Modify CSS in /static/sitecss/...

### 3. Test locally
python3 -m http.server 8000
Visit http://localhost:8000

### 4. Commit and push changes
git add .
git commit -m "Describe your changes"
git push origin main

### 5. Automatic deployment
- Changes pushed to GitHub automatically deploy to Cloudflare Workers
- Takes about 1-2 minutes to go live
- Check deployment status at: https://dash.cloudflare.com

## Common Tasks

### Adding a new page
1. Create new HTML file (e.g., services.html)
2. Add navigation links in other pages
3. Commit and push

### Updating images
1. Add image to /content/ folder
2. Reference in HTML: <img src="/content/your-image.jpg">
3. Commit and push

### Changing text/content
1. Open the relevant HTML file
2. Make changes between HTML tags
3. Save, commit, and push

## Technical Details

### Cloudflare Workers
- Platform: Cloudflare Workers with Workers Sites
- Deployment: Automatic via GitHub integration
- Configuration: wrangler.toml

### GitHub Repository
- Visibility: Public (consider making private for business)
- Branch: main (all changes should be pushed here)
- URL: https://github.com/nooodle/theattic-website

## Important Notes

1. Never commit sensitive information (passwords, API keys, etc.)
2. Always test locally before pushing changes
3. Navigation links are hardcoded in HTML - update all pages when adding new ones
4. Large files: Avoid committing very large images/videos (optimize first)

## Troubleshooting

### Site not updating after push?
1. Check GitHub Actions/Cloudflare dashboard for errors
2. Wait 2-3 minutes (deployment takes time)
3. Clear browser cache (Cmd+Shift+R on Mac)

### 404 errors on pages?
- Ensure HTML files are in root directory
- Check file names match links exactly
- Links should use .html extension

### Styling not showing?
- Check CSS file paths in HTML
- Ensure CSS files are in /static/ folder
- Clear browser cache

## Support

For deployment issues:
- Cloudflare Workers: https://developers.cloudflare.com/workers/
- GitHub: https://github.com/nooodle/theattic-website/issues

## Security Recommendations

1. Make repository private:
   - Go to GitHub Settings → General → Change visibility
   - Cloudflare will still be able to access it

2. Use environment variables for any future API keys:
   - Set in Cloudflare dashboard, not in code

3. Regular backups:
   - GitHub serves as backup
   - Consider additional local backups

---
Last updated: July 10, 2025
Migrated from Squarespace to Cloudflare Workers
