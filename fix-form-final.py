import re

# Read the contact.html file
with open('contact.html', 'r') as f:
    content = f.read()

# Remove ALL onsubmit handlers and their return false wrappers
content = re.sub(r'onsubmit="return \(function[^}]+}\)\(this\);"', '', content, flags=re.DOTALL)
content = re.sub(r'onsubmit="[^"]*"', '', content)

# Fix the phone field - replace the complex 3-field setup with a single field
phone_section = '''<div class="form-item field text required" id="phone-yui_3_17_2_1_1414013890624_19965">
<label class="title" for="phone-field">
              Phone
              
                <span aria-hidden="true" class="required">*</span>
</label>
<input aria-required="true" class="field-element text" id="phone-field" name="phone" type="tel" placeholder="0423 107 119" required/>
</div>'''

# Replace the complex phone fieldset
content = re.sub(
    r'<fieldset class="form-item fields phone required"[^>]*>.*?</fieldset>',
    phone_section,
    content,
    flags=re.DOTALL
)

# Fix the suburb field to have a name attribute
content = re.sub(
    r'<input class="field-element text" id="text-yui_3_17_2_1_1414013890624_18465-field" type="text"/>',
    '<input class="field-element text" id="text-yui_3_17_2_1_1414013890624_18465-field" name="suburb" type="text"/>',
    content
)

# Fix the textarea to have name="message"
content = re.sub(
    r'<textarea aria-required="true" class="field-element" id="textarea-yui_3_17_2_1_1414013890624_14377-field"></textarea>',
    '<textarea aria-required="true" class="field-element" id="textarea-yui_3_17_2_1_1414013890624_14377-field" name="message" required></textarea>',
    content
)

# Make sure first and last names have correct name attributes
content = re.sub(r'name="fname"', 'name="first_name"', content)
content = re.sub(r'name="lname"', 'name="last_name"', content)

# Save the updated file
with open('contact.html', 'w') as f:
    f.write(content)

print("✅ Form fixed - removed JavaScript interference and fixed field names")
