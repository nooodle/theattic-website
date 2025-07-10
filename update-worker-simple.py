# Create a simpler Worker that handles assets correctly
worker_content = '''export default {
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

    // Handle root
    if (pathname === '/') {
      pathname = '/index.html';
    } else if (!pathname.includes('.')) {
      // Add .html to paths without extension
      pathname = pathname + '.html';
    }

    // For contact page, inject Turnstile key
    if (pathname === '/contact.html' || pathname === '/contact') {
      try {
        // Try to fetch the contact page
        const response = await fetch(new URL(pathname, request.url));
        
        if (response.ok) {
          let text = await response.text();
          
          // Inject Turnstile site key if available
          if (env.TURNSTILE_SITE_KEY) {
            text = text.replace(
              'TURNSTILE_SITE_KEY_PLACEHOLDER',
              env.TURNSTILE_SITE_KEY
            );
          }
          
          return new Response(text, {
            headers: {
              'content-type': 'text/html;charset=UTF-8',
            },
          });
        }
      } catch (e) {
        console.error('Error fetching contact page:', e);
      }
    }

    // Default: pass through the request
    return fetch(new URL(pathname, request.url));
  }
};
'''

with open('workers-site/index.js', 'w') as f:
    f.write(worker_content)
    
print("✅ Updated Worker with simpler asset handling")
