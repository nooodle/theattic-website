import re
import os

nav_script = '''<script>
    // Highlight current page in navigation
    document.addEventListener('DOMContentLoaded', function() {
        const currentPath = window.location.pathname;
        const navLinks = document.querySelectorAll('#topNav a, .nav-item a');
        
        navLinks.forEach(link => {
            const href = link.getAttribute('href');
            if (href === currentPath || href === currentPath + '.html' || 
                (currentPath === '/' && (href === 'index.html' || href === '/'))) {
                link.style.borderBottom = '2px solid #333';
                link.style.paddingBottom = '2px';
            }
        });
    });
    </script>
</body>'''

html_files = ['index.html', 'about.html', 'contact.html', 'project-5.html', 'new-gallery-5.html']

for filename in html_files:
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            content = f.read()
        
        if 'Highlight current page' not in content:
            content = re.sub(r'</body>', nav_script, content)
            
            with open(filename, 'w') as f:
                f.write(content)
                
            print(f"✅ Added nav highlighting to {filename}")
