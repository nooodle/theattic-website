import re
import os

# Add Google Fonts as a more reliable option
google_fonts = '''<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Work+Sans:wght@300;400;700&display=swap" rel="stylesheet">
<style>
/* Use Work Sans as a close alternative to Brandon Grotesque */
body, html {
    font-family: "brandon-grotesque", "Work Sans", "Helvetica Neue", Helvetica, Arial, sans-serif !important;
    font-weight: 400;
}
h1, h2, h3, h4, h5, h6 {
    font-family: "brandon-grotesque", "Work Sans", "Helvetica Neue", Helvetica, Arial, sans-serif !important;
}
</style>
</head>'''

html_files = ['index.html', 'about.html', 'contact.html', 'project-5.html', 'new-gallery-5.html', 'thank-you.html']

for filename in html_files:
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            content = f.read()
        
        # Add Google Fonts before </head>
        if 'fonts.googleapis.com' not in content:
            content = re.sub(r'</head>', google_fonts, content)
            
            with open(filename, 'w') as f:
                f.write(content)
            
            print(f"✅ Added Google Fonts to {filename}")

print("\n✅ Added Google Fonts as fallback!")
