# Add debugging to the Worker
worker_content = '''export default {
  async fetch(request, env, ctx) {
    const url = new URL(request.url);
    let pathname = url.pathname;

    // Debug logging
    console.log('Request pathname:', pathname);
    console.log('TURNSTILE_SITE_KEY exists:', !!env.TURNSTILE_SITE_KEY);

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
      console.log('Processing contact page');
      
      try {
        // Fetch the original request
        const response = await fetch(request);
        
        if (response.ok) {
          let text = await response.text();
          
          // Check if placeholder exists
          if (text.includes('TURNSTILE_SITE_KEY_PLACEHOLDER')) {
            console.log('Found placeholder, replacing...');
            
            if (env.TURNSTILE_SITE_KEY) {
              console.log('Replacing with site key');
              text = text.replace(
                'TURNSTILE_SITE_KEY_PLACEHOLDER',
                env.TURNSTILE_SITE_KEY
              );
            } else {
              console.error('TURNSTILE_SITE_KEY not found in env!');
              // For debugging, show what env vars are available
              console.log('Available env vars:', Object.keys(env));
            }
          }
          
          return new Response(text, {
            headers: response.headers,
          });
        }
      } catch (e) {
        console.error('Error processing contact page:', e);
      }
    }

    // Default: pass through the request
    return fetch(request);
  }
};
'''

with open('workers-site/index.js', 'w') as f:
    f.write(worker_content)
    
print("✅ Added debugging to Worker")
