import re

# Update to use modern Workers with Assets binding
updated_content = '''export default {
  async fetch(request, env, ctx) {
    const url = new URL(request.url);
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
        // Try with .html extension
        const htmlPath = pathname + '.html';
        const htmlRequest = new Request(new URL(htmlPath, request.url), request);
        const htmlResponse = await env.ASSETS.fetch(htmlRequest);
        
        if (htmlResponse.status === 200) {
          pathname = htmlPath;
          request = htmlRequest;
        }
      }

      // Fetch the asset
      let response = await env.ASSETS.fetch(request);

      // Special handling for contact page - inject Turnstile key
      if ((pathname === '/contact.html' || pathname === '/contact') && response.status === 200) {
        const text = await response.text();
        
        // Use the environment variable set in Cloudflare dashboard
        if (env.TURNSTILE_SITE_KEY) {
          const modifiedHtml = text.replace(
            'TURNSTILE_SITE_KEY_PLACEHOLDER',
            env.TURNSTILE_SITE_KEY
          );
          
          return new Response(modifiedHtml, {
            status: response.status,
            statusText: response.statusText,
            headers: response.headers
          });
        } else {
          console.error('TURNSTILE_SITE_KEY not found in environment variables');
        }
      }

      return response;
    } catch (e) {
      return new Response('Not found: ' + e.message, { status: 404 });
    }
  }
};
'''

with open('workers-site/index.js', 'w') as f:
    f.write(updated_content)
    
print("✅ Updated Worker to use modern Assets binding")
