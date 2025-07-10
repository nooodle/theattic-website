const fs = require('fs');

// Read HTML files
const files = {
  'index': fs.readFileSync('index.html', 'utf8'),
  'about': fs.readFileSync('about.html', 'utf8'),
  'contact': fs.readFileSync('contact.html', 'utf8'),
  'project-5': fs.readFileSync('project-5.html', 'utf8'),
  'new-gallery-5': fs.readFileSync('new-gallery-5.html', 'utf8')
};

// Create the Worker script
const workerScript = `
const htmlContent = ${JSON.stringify(files, null, 2)};

export default {
  async fetch(request) {
    const url = new URL(request.url);
    let path = url.pathname;
    
    if (path === '/') path = '/index';
    path = path.replace('.html', '').substring(1) || 'index';
    
    const html = htmlContent[path];
    
    if (html) {
      return new Response(html, {
        headers: { 'content-type': 'text/html;charset=UTF-8' }
      });
    }
    
    return new Response('Page not found', { status: 404 });
  }
};
`;

fs.writeFileSync('index.js', workerScript);
console.log('Worker built successfully!');
