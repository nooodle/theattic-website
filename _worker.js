export default {
  async fetch(request, env) {
    const url = new URL(request.url);
    let path = url.pathname;
    
    // Map clean URLs to HTML files
    if (path === '/') {
      path = '/index.html';
    } else if (!path.includes('.') && !path.endsWith('/')) {
      // Try adding .html to paths without extensions
      const htmlPath = path + '.html';
      const response = await env.ASSETS.fetch(
        new Request(new URL(htmlPath, request.url), request)
      );
      if (response.status === 200) {
        return response;
      }
    }
    
    // Fetch the asset
    return env.ASSETS.fetch(request);
  }
};
