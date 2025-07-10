export default {
  async fetch(request) {
    const url = new URL(request.url);
    const path = url.pathname;
    
    // For now, let's just get your homepage working
    if (path === '/' || path === '/index.html') {
      // Read the index.html file content
      const html = await fetch(new URL('./index.html', import.meta.url)).then(r => r.text()).catch(() => null);
      
      if (html) {
        return new Response(html, {
          headers: { 'content-type': 'text/html' }
        });
      }
    }
    
    // For other paths, return the HTML files
    const htmlFile = path.endsWith('.html') ? path : `${path}.html`;
    try {
      const response = await fetch(new URL(`.${htmlFile}`, import.meta.url));
      if (response.ok) {
        const content = await response.text();
        return new Response(content, {
          headers: { 'content-type': 'text/html' }
        });
      }
    } catch (e) {
      // File not found
    }
    
    return new Response('Page not found', { status: 404 });
  }
};
