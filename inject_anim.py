import re

# Road animation HTML
road = (
    '<div class="road-scene" aria-hidden="true">'
    '<div class="cloud c1">&#9729;</div>'
    '<div class="cloud c2">&#9729;</div>'
    '<div class="cloud c3">&#9729;</div>'
    '<div class="road">'
    '<div class="road-line"></div><div class="road-line"></div>'
    '<div class="road-line"></div><div class="road-line"></div>'
    '<div class="road-line"></div><div class="road-line"></div>'
    '<div class="road-line"></div>'
    '</div>'
    '<div class="vehicle v1">&#128663;</div>'
    '<div class="vehicle v2">&#128653;</div>'
    '<div class="vehicle v3">&#128657;</div>'
    '<div class="vehicle v4">&#128665;</div>'
    '</div>'
)

js = (
    '<script>'
    'window.addEventListener("scroll",function(){'
    'document.getElementById("navbar").classList.toggle("scrolled",window.scrollY>50);'
    '});'
    'var obs=new IntersectionObserver(function(entries){'
    'entries.forEach(function(e){if(e.isIntersecting)e.target.classList.add("visible");});'
    '},{threshold:0.12});'
    'document.querySelectorAll(".reveal,.reveal-left,.reveal-right").forEach(function(el){obs.observe(el);});'
    '</script>'
)

with open(r'c:\Users\asus\Documents\Company Project\index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Inject road scene before closing hero section
marker = '</section>\n\n<!-- ABOUT STRIP -->'
if marker in html:
    html = html.replace(marker, road + '\n</section>\n\n<!-- ABOUT STRIP -->', 1)
    print('Road scene injected')
else:
    print('Marker not found, trying alternate...')
    # Try alternate
    alt = '</section>'
    idx = html.find('<!-- ABOUT STRIP -->')
    if idx > 0:
        close_idx = html.rfind('</section>', 0, idx)
        html = html[:close_idx] + road + '\n</section>' + html[close_idx+10:]
        print('Road scene injected via alternate')

# Inject JS before </body>
html = html.replace('</body>', js + '\n</body>', 1)

with open(r'c:\Users\asus\Documents\Company Project\index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print('Done. File size:', len(html))
