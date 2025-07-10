import os
import re

# Favicon HTML to add
favicon_html = '''<link rel="icon" type="image/x-icon" href="/favicon.ico">
<link rel="icon" type="image/png" sizes="32x32" href="/favicons/favicon-32x32.png">
<link rel="icon" type="image/png" sizes="16x16" href="/favicons/favicon-16x16.png">
<link rel="apple-touch-icon" sizes="180x180" href="/favicons/apple-touch-icon.png">
<link rel="icon" type="image/png" sizes="192x192" href="/favicons/android-chrome-192x192.png">
<link rel="icon" type="image/png" sizes="512x512" href="/favicons/android-chrome-512x512.png">
</head>'''

# List of HTML files
html_files = ['index.html', 'about.html', 'contact.html', 'project-5.html', 'new-gallery-5.html', 'thank-you.html']

for filename in html_files:
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            content = f.read()
        
        # Check if favicon already exists
        if 'favicon' not in content:
            # Add favicon links before </head>
            content = re.sub(r'</head>', favicon_html, content)
            
            with open(filename, 'w') as f:
                f.write(content)
            
            print(f"✅ Added favicon to {filename}")
        else:
            print(f"ℹ️ Favicon already exists in {filename}")

print("\n✅ Favicon setup complete!")
