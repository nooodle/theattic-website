export default {
  async fetch(request, env, ctx) {
    const url = new URL(request.url);
    let pathname = url.pathname;

    // Redirect www to non-www
    if (url.hostname === 'www.theattic.net.au') {
      return Response.redirect('https://theattic.net.au' + url.pathname, 301);
    }
    
    // Handle root
    if (pathname === '/') {
      pathname = '/index.html';
    } else if (!pathname.includes('.')) {
      pathname = pathname + '.html';
    }

    // Construct the asset URL
    const assetURL = new URL(pathname, request.url);
    let response = await fetch(assetURL);

    // For contact page, inject Turnstile key
    if ((pathname === '/contact.html' || pathname === '/contact') && response.ok) {
      const text = await response.text();
      
      if (text.includes('TURNSTILE_SITE_KEY_PLACEHOLDER') && env.TURNSTILE_SITE_KEY) {
        const modifiedText = text.replace(
          'TURNSTILE_SITE_KEY_PLACEHOLDER',
          env.TURNSTILE_SITE_KEY
        );
        
        return new Response(modifiedText, {
          headers: response.headers
        });
      }
    }

    return response;
  }
};
