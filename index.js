// Simple static file server
const htmlFiles = {
  '/': 'index.html',
  '/index.html': 'index.html',
  '/about': 'about.html',
  '/about.html': 'about.html',
  '/contact': 'contact.html',
  '/contact.html': 'contact.html',
  '/project-5': 'project-5.html',
  '/project-5.html': 'project-5.html',
  '/new-gallery-5': 'new-gallery-5.html',
  '/new-gallery-5.html': 'new-gallery-5.html'
};

export default {
  async fetch(request) {
    const url = new URL(request.url);
    const path = url.pathname;
    
    // Check if we have this route
    const htmlFile = htmlFiles[path] || htmlFiles[path + '.html'];
    
    if (htmlFile) {
      // For now, return a message (we'll fix this after it deploys)
      return new Response(`Loading ${htmlFile}...`, {
        headers: { 'content-type': 'text/html' }
      });
    }
    
    return new Response('Not found', { status: 404 });
  }
};
