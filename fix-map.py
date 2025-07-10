import re

with open('contact.html', 'r') as f:
    content = f.read()

# The current map shows wrong address (Spotswood), let's fix it with correct Collingwood address
new_map_html = '''<div class="sqs-block map-block sqs-block-map sized vsize-12" id="block-yui_3_17_2_1_1414013890624_22062">
<div class="sqs-block-content">
<div style="height: 400px; width: 100%; background: #f0f0f0;">
    <iframe 
        src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3152.016706!2d144.9810564!3d-37.8031231!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x6ad6430a4763b7c3%3A0x4c4c1b8969e5e4f5!2s33%20Sackville%20St%2C%20Collingwood%20VIC%203066%2C%20Australia!5e0!3m2!1sen!2sau!4v1699999999999!5m2!1sen!2sau" 
        width="100%" 
        height="400" 
        style="border:0;" 
        allowfullscreen="" 
        loading="lazy"
        referrerpolicy="no-referrer-when-downgrade">
    </iframe>
</div>
</div>
</div>'''

# Replace the entire map block
pattern = r'<div class="sqs-block website-component-block sqs-block-website-component map-block sqs-block-map[^>]*>.*?</div>\s*</div>\s*</div>'
content = re.sub(pattern, new_map_html, content, flags=re.DOTALL)

# Save
with open('contact.html', 'w') as f:
    f.write(content)
    
print("✅ Replaced Squarespace map with Google Maps iframe")
print("✅ Fixed address to show 33 Sackville St, Collingwood")
