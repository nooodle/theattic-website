import re
import os

# Clean, modern font stack using Inter from Google Fonts
font_fix = '''<link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;700&display=swap" rel="stylesheet">
    <style>
    /* Clean, modern typography */
    body, html {
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif !important;
        font-weight: 400;
        font-size: 16px;
        line-height: 1.6;
        color: #333;
        -webkit-font-smoothing: antialiased;
        -moz-osx-font-smoothing: grayscale;
    }
    
    h1, h2, h3, h4, h5, h6 {
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif !important;
        font-weight: 700;
        line-height: 1.2;
        color: #000;
    }
    
    /* Fix navigation font */
    #topNav a, .nav-item a {
        font-family: 'Inter', sans-serif !important;
        font-weight: 500;
        letter-spacing: 0.5px;
    }
    
    /* Form typography */
    input, textarea, select, button {
        font-family: 'Inter', sans-serif !important;
    }
    </style>
'''

html_files = ['index.html', 'about.html', 'contact.html', 'project-5.html', 'new-gallery-5.html', 'thank-you.html']

for filename in html_files:
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            content = f.read()
        
        # Remove old font imports
        content = re.sub(r'<link[^>]*typekit[^>]*>', '', content)
        content = re.sub(r'<script[^>]*typekit[^>]*>.*?</script>', '', content, flags=re.DOTALL)
        
        # Add new fonts before </head>
        if 'Inter' not in content:
            content = re.sub(r'</head>', font_fix + '\n</head>', content)
        
        with open(filename, 'w') as f:
            f.write(content)
            
        print(f"✅ Fixed fonts in {filename}")
