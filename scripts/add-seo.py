import re
import os

seo_tags = '''<meta name="description" content="Attic Building Design - Professional architectural design services in Melbourne and Tasmania">
<meta property="og:title" content="Attic Building Design">
<meta property="og:description" content="Professional architectural design services">
<meta property="og:image" content="https://theattic.net.au/content/v1/5368b369e4b010f43961a262/1399373038035-4A5NA9WLQ4UHR1L70BU5/AtticLogo_BLACK.png">
<meta property="og:url" content="https://theattic.net.au">
<meta name="twitter:card" content="summary_large_image">
'''

for file in ['index.html', 'about.html', 'contact.html', 'project-5.html', 'new-gallery-5.html']:
    if os.path.exists(file):
        with open(file, 'r') as f:
            content = f.read()
        if 'og:title' not in content:
            content = re.sub(r'(<head[^>]*>)', r'\1\n' + seo_tags, content)
            with open(file, 'w') as f:
                f.write(content)
