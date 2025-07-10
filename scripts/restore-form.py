import re

with open('contact.html', 'r') as f:
    content = f.read()

# Find where the form should be (after CONTACT US heading)
# Look for the pattern where the form was supposed to be
form_html = '''<div class="sqs-block form-block sqs-block-form" data-block-type="9">
<div class="sqs-block-content">
<div class="form-wrapper">
<div class="form-inner-wrapper">
<form action="https://formspree.io/f/xeokyqjr" method="POST">
  <input type="hidden" name="_subject" value="New contact from The Attic website">
  <input type="hidden" name="_next" value="https://theattic.nikvalentine.workers.dev/thank-you.html">
  <input type="text" name="_gotcha" style="display:none">
  
  <div class="field-list clear">
    <fieldset class="form-item fields name required">
      <legend class="title">Name <span class="required">*</span></legend>
      <div class="field first-name">
        <label class="caption">
          <input type="text" name="first_name" required class="field-element field-control" maxlength="30">
          <span class="caption-text">First Name</span>
        </label>
      </div>
      <div class="field last-name">
        <label class="caption">
          <input type="text" name="last_name" required class="field-element field-control" maxlength="30">
          <span class="caption-text">Last Name</span>
        </label>
      </div>
    </fieldset>
    
    <div class="form-item field text">
      <label class="title" for="suburb-field">Suburb</label>
      <input type="text" name="suburb" id="suburb-field" class="field-element text">
    </div>
    
    <div class="form-item field text required">
      <label class="title" for="phone-field">Phone <span class="required">*</span></label>
      <input type="tel" name="phone" id="phone-field" required class="field-element text">
    </div>
    
    <div class="form-item field email required">
      <label class="title" for="email-field">Email Address <span class="required">*</span></label>
      <input type="email" name="email" id="email-field" required class="field-element">
    </div>
    
    <div class="form-item field textarea required">
      <label class="title" for="message-field">Brief Description <span class="required">*</span></label>
      <textarea name="message" id="message-field" required class="field-element"></textarea>
    </div>
  </div>
  
  <div class="form-button-wrapper form-button-wrapper--align-left">
    <input type="submit" value="Submit" class="button sqs-system-button sqs-editable-button">
  </div>
</form>
</div>
</div>
</div>
</div>'''

# Find where to insert the form - after the CONTACT US heading
pattern = r'(<h1[^>]*>CONTACT US[^<]*</h1>\s*</div>\s*</div>\s*</div>)'
replacement = r'\1' + form_html

# Replace
content = re.sub(pattern, replacement, content)

# Save
with open('contact.html', 'w') as f:
    f.write(content)
    
print("✅ Restored contact form")
