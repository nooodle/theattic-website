import { handleContactForm, injectTurnstileKey } from './contact-handler.js';
import { getAssetFromKV } from '@cloudflare/kv-asset-handler';

addEventListener('fetch', event => {
  event.respondWith(handleRequest(event));
});


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

