import re

# Read current worker
with open('workers-site/index.js', 'r') as f:
    content = f.read()

# Add import at the top
import_statement = "import { handleContactForm, injectTurnstileKey } from './contact-handler.js';\n"
if 'handleContactForm' not in content:
    content = import_statement + content

# Update the fetch handler to handle contact form and inject keys
updated_handler = '''
async function handleRequest(event) {
  const url = new URL(event.request.url);
  
  // Handle contact form POST
  if (url.pathname === '/contact' && event.request.method === 'POST') {
    return handleContactForm(event.request, env);
  }
  
  try {
    let response = await getAssetFromKV(event, {
      mapRequestToAsset: req => {
        const url = new URL(req.url);
        let pathname = url.pathname;
        
        if (pathname === '/') {
          pathname = '/index.html';
        } else if (!pathname.includes('.')) {
          pathname = pathname + '.html';
        }
        
        return new Request(new URL(pathname, req.url).toString(), req);
      },
    });
    
    // Inject Turnstile key for contact page
    if (url.pathname === '/contact' || url.pathname === '/contact.html') {
      response = await injectTurnstileKey(response, env);
    }
    
    return response;
  } catch (e) {
    // Try original request if modified fails
    try {
      return await getAssetFromKV(event);
    } catch (e) {
      return new Response('Not found', { status: 404 });
    }
  }
}
'''

# Find and update the handleRequest function
if 'async function handleRequest' in content:
    # Replace existing handleRequest
    pattern = r'async function handleRequest\(event\) {.*?^}'
    content = re.sub(pattern, updated_handler, content, flags=re.DOTALL | re.MULTILINE)
else:
    # Add it before the event listener
    content = updated_handler + '\n' + content

# Save
with open('workers-site/index.js', 'w') as f:
    f.write(content)
    
print("✅ Updated main Worker to handle contact form and inject keys")
