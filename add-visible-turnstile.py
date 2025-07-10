import re

with open('contact.html', 'r') as f:
    content = f.read()

# Add Turnstile script if not already there
if 'turnstile/v0/api.js' not in content:
    turnstile_script = '''<script src="https://challenges.cloudflare.com/turnstile/v0/api.js" async defer></script>
</head>'''
    content = re.sub(r'</head>', turnstile_script, content)

# Add visible Turnstile widget before submit button
turnstile_widget = '''  </div>
  
  <!-- Cloudflare Turnstile -->
  <div class="form-item" style="margin: 20px 0;">
    <div class="cf-turnstile" 
         data-sitekey="TURNSTILE_SITE_KEY_PLACEHOLDER"
         data-callback="onTurnstileSuccess"
         data-expired-callback="onTurnstileExpired"
         data-theme="light"
         data-size="normal">
    </div>
  </div>
  
  <div class="form-button-wrapper form-button-wrapper--align-left">'''

# Find and replace the area before submit button
pattern = r'(  </div>\s*\n\s*<div class="form-button-wrapper[^>]*>)'
content = re.sub(pattern, turnstile_widget, content)

# Update submit button to be disabled initially
content = re.sub(
    r'<input type="submit" value="Submit"([^>]*)>',
    '<input type="submit" value="Submit" id="submit-button" disabled\\1>',
    content
)

# Add style for disabled button
style_addition = '''<style>
#submit-button:disabled {
    opacity: 0.5;
    cursor: not-allowed;
}
.turnstile-error {
    color: #d32f2f;
    font-size: 14px;
    margin-top: 10px;
}
</style>
</head>'''
content = re.sub(r'</head>', style_addition, content)

# Add JavaScript for handling Turnstile
callback_script = '''<script>
// Enable submit button when Turnstile is completed
function onTurnstileSuccess(token) {
    document.getElementById('submit-button').disabled = false;
    // Remove any error messages
    const errorMsg = document.querySelector('.turnstile-error');
    if (errorMsg) errorMsg.remove();
}

// Disable submit button when Turnstile expires
function onTurnstileExpired() {
    document.getElementById('submit-button').disabled = true;
    // Show error message
    const turnstileDiv = document.querySelector('.cf-turnstile');
    if (turnstileDiv && !document.querySelector('.turnstile-error')) {
        const error = document.createElement('div');
        error.className = 'turnstile-error';
        error.textContent = 'Security check expired. Please complete it again.';
        turnstileDiv.parentNode.appendChild(error);
    }
}

// Form validation
document.addEventListener('DOMContentLoaded', function() {
    const form = document.querySelector('form[action="/contact"]');
    if (form) {
        form.addEventListener('submit', function(e) {
            const turnstileResponse = document.querySelector('[name="cf-turnstile-response"]');
            if (!turnstileResponse || !turnstileResponse.value) {
                e.preventDefault();
                alert('Please complete the security check before submitting.');
                return false;
            }
        });
    }
});
</script>
</body>'''
content = re.sub(r'</body>', callback_script, content)

# Change form action to submit to Worker endpoint
content = re.sub(
    r'action="https://formspree.io/f/xeokyqjr"',
    'action="/contact"',
    content
)

# Save
with open('contact.html', 'w') as f:
    f.write(content)
    
print("✅ Added visible Cloudflare Turnstile to contact form")
print("✅ Submit button is disabled until Turnstile is completed")
