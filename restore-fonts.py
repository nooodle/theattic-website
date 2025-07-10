import os
import re

# The Typekit/Adobe Fonts script from your original site
typekit_script = '''<script async="" fetchpriority="high" onload="try{Typekit.load();}catch(e){} document.documentElement.classList.remove('wf-loading');" src="//use.typekit.net/ik/9TrxDoCjXOUG3MjJsSII39R0N8YrD3P32iN2EJMtvobfe09ffFHN4UJLFRbh52jhWD9DFRyKwDjoZQsKw2I3ZRbD5QjUjQJhwy7FMPG0dc8nOWZydem0ie80ZPoDSWmyScmDSeBRZPoRdhXCdeNRjAUGdaFXOeoT-kuhjAU8d1sTdc90SaBujW48Sagyjh90jhNlOYsGZABXie8ROco8ifoyiPUaiaS0dc8nOWZydem0ie80ZPoDSWmyScmDSeBRZPoRdhXCiaiaO1sGZABXie8ROco8ifoyiPJwSY4zpe8ljPu0daZyJ68ciWsuScIlSYbKfcuuShmzOWFyd1w7fbRKHyMMeMw6MKG4fHXgIMMjgKMfH6qJK3IbMg6YJMJ7fbRRHyMMeMX6MKG4fHtgIMMjIfMfH6qJRMIbMg6sJMJ7fbKImsMgeMb6MKG4fJBmIMIjgkMfH6qJubvbMy62JMJ7fbRZ2UMfeMS6MKG4fFjVIMJj2PMfH6qJh6vbMy6sJMHbMic_TrSB.js" type="text/javascript"></script>
<script>document.documentElement.classList.add('wf-loading')</script>
<style>@keyframes fonts-loading { 0%, 99% { color: transparent; } } html.wf-loading * { animation: fonts-loading 3s; }</style>'''

# List of HTML files to update
html_files = ['index.html', 'about.html', 'contact.html', 'project-5.html', 'new-gallery-5.html', 'thank-you.html']

for filename in html_files:
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            content = f.read()
        
        # Check if Typekit is already there
        if 'typekit.net' not in content:
            # Add before closing </head>
            content = re.sub(r'(</head>)', typekit_script + r'\n\1', content)
            
            with open(filename, 'w') as f:
                f.write(content)
            
            print(f"✅ Added fonts to {filename}")
        else:
            print(f"ℹ️ Fonts already present in {filename}")

print("\n✅ Font restoration complete!")
