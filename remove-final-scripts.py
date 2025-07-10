import re

with open('contact.html', 'r') as f:
    content = f.read()

# Remove the Squarespace combo script
content = re.sub(r'<script src="[^"]*squarespace[^"]*combo[^"]*"[^>]*></script>', '', content)

# Remove any other scripts from static1.squarespace.com
content = re.sub(r'<script[^>]*src="[^"]*static1\.squarespace\.com[^"]*"[^>]*></script>', '', content)

# Save
with open('contact.html', 'w') as f:
    f.write(content)
    
print("✅ Removed remaining Squarespace scripts")
