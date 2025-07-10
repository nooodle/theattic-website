import re
import os

html_files = ['index.html', 'about.html', 'contact.html', 'project-5.html', 'new-gallery-5.html', 'thank-you.html']

for filename in html_files:
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            content = f.read()
        
        # Remove broken Squarespace scripts
        content = re.sub(r'<script[^>]*squarespace[^>]*>.*?</script>', '', content, flags=re.DOTALL)
        content = re.sub(r'<link[^>]*squarespace[^>]*>', '', content)
        content = re.sub(r'<script[^>]*static1\.squarespace[^>]*>.*?</script>', '', content, flags=re.DOTALL)
        
        # Remove empty script tags
        content = re.sub(r'<script[^>]*>\s*</script>', '', content)
        
        # Remove Squarespace meta tags
        content = re.sub(r'<meta[^>]*squarespace[^>]*>', '', content)
        
        with open(filename, 'w') as f:
            f.write(content)
            
        print(f"✅ Cleaned {filename}")

print("\n✅ Removed Squarespace scripts")
