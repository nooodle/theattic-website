import re
import os

# Add font fallback styles to ensure consistency
font_styles = '''<style>
/* Font fallbacks to match original design */
body {
    font-family: "proxima-nova", "Helvetica Neue", Helvetica, Arial, sans-serif;
    font-weight: 400;
    font-style: normal;
    font-size: 16px;
    line-height: 1.6;
    letter-spacing: 0px;
    color: #333;
}

h1, h2, h3, h4, h5, h6 {
    font-family: "proxima-nova", "Helvetica Neue", Helvetica, Arial, sans-serif;
    font-weight: 700;
    line-height: 1.2;
}

.logo-subtitle {
    font-family: "proxima-nova", "Helvetica Neue", Helvetica, Arial, sans-serif;
    font-weight: 300;
}
</style>
</head>'''

html_files = ['index.html', 'about.html', 'contact.html', 'project-5.html', 'new-gallery-5.html', 'thank-you.html']

for filename in html_files:
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            content = f.read()
        
        # Add font styles if not already present
        if 'Font fallbacks to match original design' not in content:
            content = re.sub(r'</head>', font_styles, content)
            
            with open(filename, 'w') as f:
                f.write(content)
            
            print(f"✅ Added font fallbacks to {filename}")

print("\n✅ Font fallback styles added!")
