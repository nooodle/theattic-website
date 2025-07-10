export default {
  async fetch(request, env) {
    const url = new URL(request.url);
    
    // Get the response from static assets
    const response = await env.ASSETS.fetch(request);
    
    // Only process HTML responses for contact page
    if ((url.pathname === '/contact' || url.pathname === '/contact.html') && 
        response.headers.get('content-type')?.includes('text/html')) {
      
      const html = await response.text();
      
      // Replace the placeholder with the actual site key
      if (env.TURNSTILE_SITE_KEY) {
        const modifiedHtml = html.replace(
          'TURNSTILE_SITE_KEY_PLACEHOLDER',
          env.TURNSTILE_SITE_KEY
        );
        
        return new Response(modifiedHtml, {
          status: response.status,
          statusText: response.statusText,
          headers: response.headers
        });
      }
    }
    
    // Return original response for all other requests
    return response;
  }
}
