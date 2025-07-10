import re

# Read the current worker
with open('workers-site/index.js', 'r') as f:
    content = f.read()

# Check if we're handling contact page
if 'injectTurnstileKey' not in content:
    # Add the injection logic
    injection_code = '''
// Inject Turnstile key for contact page
async function injectTurnstileKey(response, env) {
    if (!env.TURNSTILE_SITE_KEY) {
        console.error('TURNSTILE_SITE_KEY not configured');
        return response;
    }
    
    const text = await response.text();
    const modifiedHtml = text.replace(
        'TURNSTILE_SITE_KEY_PLACEHOLDER',
        env.TURNSTILE_SITE_KEY
    );
    
    return new Response(modifiedHtml, {
        headers: response.headers
    });
}
'''
    
    # Insert before the fetch handler
    content = injection_code + '\n' + content
    
    # Find where contact.html is served and add injection
    pattern = r'(if \(pathname === \'/contact\.html\'\) {[^}]+})'
    if not re.search(pattern, content):
        # Add handling for contact page
        contact_handling = '''
    // Handle contact page - inject Turnstile key
    if (pathname === '/contact.html' || pathname === '/contact') {
        let response = await env.ASSETS.fetch(request);
        if (response.status === 200) {
            response = await injectTurnstileKey(response, env);
        }
        return response;
    }
'''
        # Insert after pathname handling
        content = re.sub(
            r'(pathname = \'/index\.html\';)',
            r'\1\n' + contact_handling,
            content
        )

# Save the updated worker
with open('workers-site/index.js', 'w') as f:
    f.write(content)

print("✅ Fixed Turnstile injection in Worker")
