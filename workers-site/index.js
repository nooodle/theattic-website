import { getAssetFromKV } from '@cloudflare/kv-asset-handler';

addEventListener('fetch', event => {
  event.respondWith(handleRequest(event));
});

async function handleRequest(event) {
  try {
    const url = new URL(event.request.url);
    let pathname = url.pathname;

    // Handle root and clean URLs
    if (pathname === '/') {
      pathname = '/index.html';
    } else if (!pathname.includes('.')) {
      pathname = pathname + '.html';
    }

    // Create modified request with new pathname
    const modifiedRequest = new Request(url.origin + pathname, event.request);
    
    return await getAssetFromKV(event, {
      mapRequestToAsset: req => modifiedRequest,
    });
  } catch (e) {
    // Try original path if modified path fails
    try {
      return await getAssetFromKV(event);
    } catch (e) {
      return new Response('Not found', { status: 404 });
    }
  }
}
