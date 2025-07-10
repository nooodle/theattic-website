import re
import os

# Add debugging for font loading
font_debug = '''<script>
// Debug font loading
if (window.Typekit) {
    console.log('Typekit loaded successfully');
    window.Typekit.load({
        active: function() {
            console.log('Fonts loaded:', document.documentElement.className);
        },
        inactive: function() {
            console.log('Fonts failed to load');
        }
    });
}
</script>
</head>'''

html_files = ['contact.html']

for filename in html_files:
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            content = f.read()
        
        # Add debug script
        content = re.sub(r'</head>', font_debug, content)
        
        with open(filename, 'w') as f:
            f.write(content)
        
        print(f"Added font debugging to {filename}")
