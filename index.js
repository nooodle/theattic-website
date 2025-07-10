// Import your HTML files as raw text
import indexHTML from './index.html?raw';
import aboutHTML from './about.html?raw';
import contactHTML from './contact.html?raw';
import project5HTML from './project-5.html?raw';
import gallery5HTML from './new-gallery-5.html?raw';

const routes = {
  '/': indexHTML,
  '/index.html': indexHTML,
  '/about': aboutHTML,
  '/about.html': aboutHTML,
  '/contact': contactHTML,
  '/contact.html': contactHTML,
  '/project-5': project5HTML,
  '/project-5.html': project5HTML,
  '/new-gallery-5': gallery5HTML,
  '/new-gallery-5.html': gallery5HTML
};

export default {
  async fetch(request) {
    const url = new URL(request.url);
    const path = url.pathname;
    
    const html = routes[path];
    
    if (html) {
      return new Response(html, {
        headers: {
          'content-type': 'text/html;charset=UTF-8',
        },
      });
    }
    
    return new Response('Page not found', { status: 404 });
  }
};
