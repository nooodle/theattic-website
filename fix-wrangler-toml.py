# Create a clean wrangler.toml
wrangler_content = '''name = "theattic"
main = "workers-site/index.js"
compatibility_date = "2024-01-01"

# Workers with static assets configuration
# No need for [site] section with modern Workers
'''

with open('wrangler.toml', 'w') as f:
    f.write(wrangler_content)
    
print("✅ Created clean wrangler.toml")
