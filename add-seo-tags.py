import re
import os

def add_seo_to_file(filename, title_suffix=""):
    if not os.path.exists(filename):
        return
        
    with open(filename, 'r') as f:
        content = f.read()
    
    # Skip if already has og:title
    if 'og:title' in content:
        return
    
    page_title = title_suffix if title_suffix else "Professional Architectural Design"
    
    seo_tags = f'''<!-- SEO Meta Tags -->
    <meta name="description" content="Attic Building Design - {page_title} services in Melbourne and Tasmania. Creating thoughtful, sustainable architectural solutions.">
    <meta name="keywords" content="architecture, building design, melbourne architect, tasmania architect, sustainable design, residential design">
    <meta name="author" content="Attic Building Design">
    
    <!-- Open Graph / Facebook -->
    <meta property="og:type" content="website">
    <meta property="og:url" content="https://theattic.net.au">
    <meta property="og:title" content="Attic Building Design - {page_title}">
    <meta property="og:description" content="Professional architectural design services in Melbourne and Tasmania">
    <meta property="og:image" content="https://theattic.net.au/content/v1/5368b369e4b010f43961a262/1399373038035-4A5NA9WLQ4UHR1L70BU5/AtticLogo_BLACK.png">
    
    <!-- Twitter -->
    <meta property="twitter:card" content="summary_large_image">
    <meta property="twitter:url" content="https://theattic.net.au">
    <meta property="twitter:title" content="Attic Building Design">
    <meta property="twitter:description" content="Professional architectural design services">
    <meta property="twitter:image" content="https://theattic.net.au/content/v1/5368b369e4b010f43961a262/1399373038035-4A5NA9WLQ4UHR1L70BU5/AtticLogo_BLACK.png">
    '''
    
    # Add after <head> tag
    content = re.sub(r'(<head[^>]*>)', r'\1\n' + seo_tags, content)
    
    with open(filename, 'w') as f:
        f.write(content)
    
    print(f"✅ Added SEO to {filename}")

# Add to each page with appropriate titles
add_seo_to_file('index.html', 'Home')
add_seo_to_file('about.html', 'About Us')
add_seo_to_file('contact.html', 'Contact')
add_seo_to_file('project-5.html', 'Projects')
add_seo_to_file('new-gallery-5.html', 'Gallery')
add_seo_to_file('thank-you.html', 'Thank You')
