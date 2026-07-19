import re

# 1. Remove road scene from index.html
with open(r'c:\Users\asus\Documents\Company Project\index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Remove the road scene block
html = re.sub(r'\s*<!-- ANIMATED ROAD SCENE -->.*?</div>\s*(?=\n</section>)', '', html, flags=re.DOTALL)

with open(r'c:\Users\asus\Documents\Company Project\index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print('Road scene removed from index.html')

# 2. Remove road animation CSS from animations.css
with open(r'c:\Users\asus\Documents\Company Project\animations.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Remove everything from road-scene to end of vehicle/cloud section
css = re.sub(r'/\* ===== MOVING ROAD ANIMATION =====.*?/\* ===== HERO EXTRA =====.*?\}\n', '', css, flags=re.DOTALL)
# Also remove HERO EXTRA block
css = re.sub(r'/\* ===== HERO EXTRA =====.*?!\s*important;\s*\}', '', css, flags=re.DOTALL)

with open(r'c:\Users\asus\Documents\Company Project\animations.css', 'w', encoding='utf-8') as f:
    f.write(css)

print('Road CSS removed from animations.css')
print('Done.')
