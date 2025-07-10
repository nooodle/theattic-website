import re

# Read contact.html
with open('contact.html', 'r') as f:
    content = f.read()

# Google Maps URL with black and white styling
new_map_url = '''https://maps.google.com/maps?width=100%25&amp;height=400&amp;hl=en&amp;q=33%20Sackville%20St,%20Collingwood%20VIC%203066,%20Australia&amp;t=&amp;z=15&amp;ie=UTF8&amp;iwloc=B&amp;output=embed&amp;style=feature:all|element:all|saturation:-100'''

# Replace the current map URL
pattern = r'src="https://www\.google\.com/maps/embed[^"]*"'
replacement = f'src="{new_map_url}"'

content = re.sub(pattern, replacement, content)

# Also add CSS filter as backup
if 'map-filter-grayscale' not in content:
    # Add CSS for grayscale filter
    css_addition = '''<style>
/* Black and white map */
.sqs-block-map iframe {
    filter: grayscale(100%);
    -webkit-filter: grayscale(100%);
}
</style>
</head>'''
    content = re.sub(r'</head>', css_addition, content)

# Save
with open('contact.html', 'w') as f:
    f.write(content)

print("✅ Updated map to black and white style")
