import { getAssetFromKV } from '@cloudflare/kv-asset-handler';

addEventListener('fetch', event => {
  event.respondWith(handleEvent(event));
});

async function handleEvent(event) {
  const url = new URL(event.request.url);
  let pathname = url.pathname;

  // Redirect www to non-www
  if (url.hostname === 'www.theattic.net.au') {
    return Response.redirect('https://theattic.net.au' + pathname, 301);
  }

  try {
    // Handle clean URLs
    if (pathname === '/') {
      pathname = '/index.html';
    } else if (!pathname.includes('.')) {
      pathname = pathname + '.html';
    }

    // Get the asset
    const page = await getAssetFromKV(event, {
      mapRequestToAsset: req => new Request(`${url.origin}${pathname}`, req),
    });

    // For contact page, inject Turnstile key
    if (pathname === '/contact.html' && event.env && event.env.TURNSTILE_SITE_KEY) {
      const text = await page.text();
      
      if (text.includes('TURNSTILE_SITE_KEY_PLACEHOLDER')) {
        const modifiedText = text.replace(
          'TURNSTILE_SITE_KEY_PLACEHOLDER',
          event.env.TURNSTILE_SITE_KEY
        );
        
        return new Response(modifiedText, {
          headers: page.headers
        });
      }
    }

    return page;
  } catch (e) {
    // Try the original request if our modified one fails
    try {
      return await getAssetFromKV(event);
    } catch (e) {
      return new Response('Not found', { status: 404 });
    }
  }
}
