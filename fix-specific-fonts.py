import re
import os

# More specific font styles matching Squarespace defaults
specific_font_styles = '''<style>
/* Override with specific Squarespace fonts */
body, html {
    font-family: "brandon-grotesque", "Helvetica Neue", Helvetica, Arial, sans-serif !important;
    font-weight: 400;
    font-style: normal;
    font-size: 13px;
    letter-spacing: 0px;
    font-weight: 400;
    font-style: normal;
    line-height: 1.8em;
    color: #666;
}

h1, h2, h3, h4, h5, h6 {
    font-family: "brandon-grotesque", "Helvetica Neue", Helvetica, Arial, sans-serif !important;
    font-weight: 700;
    letter-spacing: 0px;
    line-height: 1.2em;
    color: #333;
}

.logo-subtitle {
    font-family: "brandon-grotesque", "Helvetica Neue", Helvetica, Arial, sans-serif !important;
    font-weight: 300;
    font-style: normal;
    font-size: 13px;
    letter-spacing: .06em;
    line-height: 1.1em;
}

/* Contact form specific styles */
.form-wrapper {
    font-family: "brandon-grotesque", "Helvetica Neue", Helvetica, Arial, sans-serif !important;
}

/* Force all text elements */
p, div, span, label, input, textarea {
    font-family: inherit !important;
}
</style>
</head>'''

html_files = ['index.html', 'about.html', 'contact.html', 'project-5.html', 'new-gallery-5.html', 'thank-you.html']

for filename in html_files:
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            content = f.read()
        
        # Remove old font fallback styles
        content = re.sub(r'<style>\s*/\* Font fallbacks.*?</style>\s*</head>', '</head>', content, flags=re.DOTALL)
        
        # Add new specific styles
        content = re.sub(r'</head>', specific_font_styles, content)
        
        with open(filename, 'w') as f:
            f.write(content)
        
        print(f"✅ Updated fonts in {filename}")

print("\n✅ Applied specific Squarespace fonts!")
