# Update wrangler.toml with proper assets configuration
wrangler_content = '''name = "theattic"
main = "workers-site/index.js"
compatibility_date = "2024-01-01"

[assets]
directory = "./"
exclude = ["workers-site", "*.md", ".git*", "*.py", "node_modules"]
'''

with open('wrangler.toml', 'w') as f:
    f.write(wrangler_content)
    
print("✅ Updated wrangler.toml with assets configuration")
