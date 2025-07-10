import re

with open('workers-site/index.js', 'r') as f:
    content = f.read()

# The Worker needs to properly pass env to handlers
# Update the event listener to pass env
updated_content = '''import { getAssetFromKV } from '@cloudflare/kv-asset-handler';

addEventListener('fetch', event => {
  event.respondWith(handleRequest(event));
});

async function handleRequest(event) {
  // Get env from the event context
  const env = event.env || {};
  const url = new URL(event.request.url);
  let pathname = url.pathname;

  // Redirect www to non-www
  if (url.hostname === 'www.theattic.net.au') {
    return Response.redirect('https://theattic.net.au' + url.pathname, 301);
  }
  
  // Force HTTPS
  if (url.protocol === 'http:') {
    return Response.redirect('https:' + url.href.substring(5), 301);
  }

  try {
    // Handle root and clean URLs
    if (pathname === '/') {
      pathname = '/index.html';
    } else if (!pathname.includes('.') && !pathname.endsWith('/')) {
      pathname = pathname + '.html';
    }

    // Create modified request
    const modifiedRequest = new Request(url.origin + pathname, event.request);
    
    // Get the asset
    let response = await getAssetFromKV(event, {
      mapRequestToAsset: req => modifiedRequest,
    });

    // Special handling for contact page - inject Turnstile key
    if (pathname === '/contact.html' || pathname === '/contact') {
      const text = await response.text();
      
      // Get the site key from wrangler.toml or environment
      const SITE_KEY = TURNSTILE_SITE_KEY || 'YOUR_SITE_KEY_HERE';
      
      const modifiedHtml = text.replace(
        'TURNSTILE_SITE_KEY_PLACEHOLDER',
        SITE_KEY
      );
      
      response = new Response(modifiedHtml, {
        headers: response.headers
      });
    }

    return response;
  } catch (e) {
    // Try original path if modified path fails
    try {
      return await getAssetFromKV(event);
    } catch (e) {
      return new Response('Not found', { status: 404 });
    }
  }
}
'''

with open('workers-site/index.js', 'w') as f:
    f.write(updated_content)
    
print("✅ Updated Worker to handle environment variables")
