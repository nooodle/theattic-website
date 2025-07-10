export default {
  async fetch(request) {
    const url = new URL(request.url);
    const path = url.pathname;
    
    // For now, let's just serve a simple HTML page to test
    const html = `<!DOCTYPE html>
<html>
<head>
    <title>The Attic</title>
    <style>
        body { font-family: Arial; text-align: center; padding: 50px; }
        a { margin: 10px; }
    </style>
</head>
<body>
    <h1>The Attic - Migration in Progress</h1>
    <p>Your site is being migrated to Cloudflare Workers.</p>
    <nav>
        <a href="/">Home</a>
        <a href="/about">About</a>
        <a href="/contact">Contact</a>
        <a href="/project-5">Project 5</a>
        <a href="/new-gallery-5">Gallery</a>
    </nav>
    <p>Requested path: ${path}</p>
</body>
</html>`;
    
    return new Response(html, {
      headers: { 'content-type': 'text/html' }
    });
  }
};
