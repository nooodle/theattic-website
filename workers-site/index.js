import { getAssetFromKV } from '@cloudflare/kv-asset-handler';

export default {
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
        pathname = pathname + '.html';
      }

      // Create modified request
      const modifiedRequest = new Request(url.origin + pathname, request);
      
      // Get the asset - note we need to create an event-like object
      const event = {
        request: modifiedRequest,
        waitUntil: ctx.waitUntil.bind(ctx),
        env: env
      };
      
      let response = await getAssetFromKV(event, {
        mapRequestToAsset: req => modifiedRequest,
      });

      // Special handling for contact page - inject Turnstile key
      if (pathname === '/contact.html' || pathname === '/contact') {
        const text = await response.text();
        
        // Use the environment variable set in Cloudflare dashboard
        if (env.TURNSTILE_SITE_KEY) {
          const modifiedHtml = text.replace(
            'TURNSTILE_SITE_KEY_PLACEHOLDER',
            env.TURNSTILE_SITE_KEY
          );
          
          response = new Response(modifiedHtml, {
            headers: response.headers
          });
        } else {
          console.error('TURNSTILE_SITE_KEY not found in environment variables');
        }
      }

      return response;
    } catch (e) {
      // Try original path if modified path fails
      try {
        const event = {
          request: request,
          waitUntil: ctx.waitUntil.bind(ctx),
          env: env
        };
        return await getAssetFromKV(event);
      } catch (e) {
        return new Response('Not found: ' + e.message, { status: 404 });
      }
    }
  }
};
