export default {
  async fetch(request, env) {
    const url = new URL(request.url);
    
    // Clean URLs - map / to /index.html, /about to /about.html
    let pathname = url.pathname;
    if (pathname === '/') {
      pathname = '/index.html';
    } else if (!pathname.includes('.') && pathname !== '/') {
      // Check if HTML file exists
      const testPath = pathname + '.html';
      request = new Request(new URL(testPath, request.url), request);
    }
    
    // Let Workers serve the static file
    return env.ASSETS.fetch(request);
  }
};
