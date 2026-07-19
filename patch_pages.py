import os, glob

pages = glob.glob(r'c:\Users\asus\Documents\Company Project\*.html')
# Exclude nav.html
pages = [p for p in pages if 'nav.html' not in p and 'inject' not in p]

head_inject = '<link rel="stylesheet" href="animations.css"/>'
body_start_inject = (
    '<div id="scroll-progress"></div>'
    '<button id="back-top" onclick="window.scrollTo({top:0,behavior:\'smooth\'})" title="Back to Top">&#8679;</button>'
)
body_end_inject = '<script src="main.js"></script>'

for path in pages:
    with open(path, 'r', encoding='utf-8') as f:
        html = f.read()

    changed = False

    if 'animations.css' not in html:
        html = html.replace('<link rel="stylesheet" href="styles.css"/>',
                            '<link rel="stylesheet" href="styles.css"/>\n' + head_inject, 1)
        changed = True

    if 'scroll-progress' not in html:
        html = html.replace('<div class="page-wrapper">', body_start_inject + '\n<div class="page-wrapper">', 1)
        changed = True

    if 'main.js' not in html:
        html = html.replace('</body>', body_end_inject + '\n</body>', 1)
        changed = True

    if changed:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(html)
        print('Updated:', os.path.basename(path))
    else:
        print('Skipped (already updated):', os.path.basename(path))

print('All done.')
