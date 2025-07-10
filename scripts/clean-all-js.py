import re

with open('contact.html', 'r') as f:
    content = f.read()

# Remove ALL script tags that contain Y.use, squarespace, or FormSubmit
content = re.sub(r'<script[^>]*>(?:(?!</script>).)*Y\.use(?:(?!</script>).)*</script>', '', content, flags=re.DOTALL)
content = re.sub(r'<script[^>]*>(?:(?!</script>).)*squarespace(?:(?!</script>).)*</script>', '', content, flags=re.DOTALL | re.IGNORECASE)
content = re.sub(r'<script[^>]*>(?:(?!</script>).)*FormSubmit(?:(?!</script>).)*</script>', '', content, flags=re.DOTALL)

# Also remove script type="module" tags that might contain form logic
content = re.sub(r'<script type="module">.*?</script>', '', content, flags=re.DOTALL)

# Remove the specific Y.use script around line 64
content = re.sub(r'<script type="module">\s*Y\.use\([^)]+\).*?</script>', '', content, flags=re.DOTALL)

# Remove any inline event handlers
content = re.sub(r'\son\w+="[^"]*"', '', content)

# Save cleaned file
with open('contact.html', 'w') as f:
    f.write(content)
    
print("✅ Removed all Squarespace JavaScript")

# Show what we found
import subprocess
result = subprocess.run(['grep', '-n', 'Y.use', 'contact.html'], capture_output=True, text=True)
if result.stdout:
    print("⚠️ Still found Y.use:")
    print(result.stdout)
else:
    print("✅ No more Y.use found")
