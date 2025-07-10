export default {
  async fetch(request) {
    const url = new URL(request.url);
    let path = url.pathname;
    
    // Map paths to your HTML files
    const routes = {
      '/': '/index.html',
      '/about': '/about.html',
      '/contact': '/contact.html',
      '/project-5': '/project-5.html',
      '/new-gallery-5': '/new-gallery-5.html'
    };
    
    // Check if we have a route for this path
    if (routes[path]) {
      path = routes[path];
    }
    
    // For now, return a message (you'll need to serve actual files)
    return new Response(`Would serve: ${path}`, {
      headers: { 'content-type': 'text/plain' },
    });
  }
};
