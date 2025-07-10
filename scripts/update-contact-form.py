import re

# Read the contact.html file
with open('contact.html', 'r') as f:
    content = f.read()

# Replace the form action and remove the onsubmit handler
content = re.sub(
    r'<form[^>]*action="[^"]*"[^>]*onsubmit="[^"]*"[^>]*>',
    '<form action="https://formspree.io/f/xeokyqjr" method="POST">',
    content,
    flags=re.IGNORECASE | re.DOTALL
)

# Fix the input names for Formspree
# First name
content = re.sub(r'name="fname"', 'name="first_name"', content)
# Last name  
content = re.sub(r'name="lname"', 'name="last_name"', content)
# Email is already correct
# Phone fields need to be combined
content = re.sub(r'<input[^>]*data-title="Areacode"[^>]*>', '<input name="phone_area" type="text" maxlength="3">', content)
content = re.sub(r'<input[^>]*data-title="Prefix"[^>]*>', '<input name="phone_prefix" type="text" maxlength="3">', content)
content = re.sub(r'<input[^>]*data-title="Line"[^>]*>', '<input name="phone_line" type="text" maxlength="4">', content)

# Suburb field
content = re.sub(
    r'<input[^>]*id="text-yui_3_17_2_1_1414013890624_18465-field"[^>]*>',
    '<input name="suburb" class="field-element text" id="text-yui_3_17_2_1_1414013890624_18465-field" type="text">',
    content
)

# Brief description textarea
content = re.sub(
    r'<textarea[^>]*id="textarea-yui_3_17_2_1_1414013890624_14377-field"[^>]*></textarea>',
    '<textarea name="message" class="field-element" id="textarea-yui_3_17_2_1_1414013890624_14377-field" aria-required="true"></textarea>',
    content
)

# Add Formspree special fields after the opening form tag
formspree_fields = '''<form action="https://formspree.io/f/xeokyqjr" method="POST">
  <input type="hidden" name="_subject" value="New contact from The Attic website">
  <input type="text" name="_gotcha" style="display:none">'''

content = re.sub(
    r'<form action="https://formspree.io/f/xeokyqjr" method="POST">',
    formspree_fields,
    content,
    count=1
)

# Save the updated file
with open('contact.html', 'w') as f:
    f.write(content)

print("✅ Contact form updated successfully!")
print("✅ Form will now send to nik@theattic.net.au via Formspree")
