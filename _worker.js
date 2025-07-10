export default {
  async fetch(request, env) {
    const url = new URL(request.url);
    
    // Debug logging
    console.log('Request URL:', url.pathname);
    console.log('Environment variables available:', Object.keys(env));
    console.log('TURNSTILE_SITE_KEY exists:', !!env.TURNSTILE_SITE_KEY);
    
    // Get the response from static assets
    const response = await env.ASSETS.fetch(request);
    
    // Only process HTML responses for contact page
    if ((url.pathname === '/contact' || url.pathname === '/contact.html')) {
      console.log('Processing contact page');
      
      if (response.headers.get('content-type')?.includes('text/html')) {
        const html = await response.text();
        
        if (html.includes('TURNSTILE_SITE_KEY_PLACEHOLDER')) {
          console.log('Found placeholder');
          
          if (env.TURNSTILE_SITE_KEY) {
            console.log('Replacing with site key');
            const modifiedHtml = html.replace(
              'TURNSTILE_SITE_KEY_PLACEHOLDER',
              env.TURNSTILE_SITE_KEY
            );
            
            return new Response(modifiedHtml, {
              status: response.status,
              statusText: response.statusText,
              headers: response.headers
            });
          } else {
            console.error('TURNSTILE_SITE_KEY not found in environment!');
          }
        }
      }
    }
    
    return response;
  }
}
