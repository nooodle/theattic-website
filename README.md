# theattic.net.au - Static Site

This is a static version of https://theattic.net.au ready for deployment to Cloudflare Pages.

## Quick Deploy to Cloudflare Pages

1. Push this repository to GitHub
2. Log in to [Cloudflare Pages](https://pages.cloudflare.com)
3. Click "Create a project"
4. Connect your GitHub account and select this repository
5. Use these build settings:
   - Build command: (leave empty)
   - Build output directory: /
6. Click "Save and Deploy"

## Local Preview

You can preview the site locally using any static server:

```bash
# Using Python
python -m http.server 8000

# Using Node.js
npx serve

# Using PHP
php -S localhost:8000
```

## Site Structure

- `index.html` - Homepage
- `*.html` - Other pages
- `/images/` - Image assets
- `/css/` - Stylesheets
- `/js/` - JavaScript files

## Notes

- Downloaded on: 2025-07-10 13:25:56
- Total pages: 6
