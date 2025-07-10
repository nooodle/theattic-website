import re

with open('wrangler.toml', 'r') as f:
    content = f.read()

# Remove old site configuration
content = re.sub(r'\[site\][^\[]*', '', content, flags=re.DOTALL)

# Ensure we have the basic configuration
if 'compatibility_date' not in content:
    content += '\ncompatibility_date = "2024-01-01"\n'

# Clean up extra newlines
content = re.sub(r'\n{3,}', '\n\n', content)

with open('wrangler.toml', 'w') as f:
    f.write(content.strip() + '\n')
    
print("✅ Cleaned up wrangler.toml")
