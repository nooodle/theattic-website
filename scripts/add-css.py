import re

with open('contact.html', 'r') as f:
    content = f.read()
    
# Add the CSS before the closing </head> tag
css_tag = '''<style>
/* Hide Squarespace form elements */
.form-submission-text,
.form-submission-html,
.sqs-form-block-submission-html {
    display: none !important;
}
</style>
</head>'''

content = re.sub(r'</head>', css_tag, content)

with open('contact.html', 'w') as f:
    f.write(content)
    
print('✅ Added CSS to hide Squarespace elements')
