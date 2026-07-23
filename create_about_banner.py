import os
from PIL import Image, ImageDraw, ImageFont, ImageFilter

# Canvas dimensions (2400 x 900 4K quality)
width = 2400
height = 900

# Create base image with deep dark navy gradient
img = Image.new("RGBA", (width, height), "#060f24")
draw = ImageDraw.Draw(img)

# Draw subtle gradient background
for y in range(height):
    r = int(6 + (10 - 6) * (y / height))
    g = int(15 + (33 - 15) * (y / height))
    b = int(36 + (71 - 36) * (y / height))
    draw.line([(0, y), (width, y)], fill=(r, g, b, 255))

# Draw subtle background tech/geometric lines
for x in range(0, width, 120):
    draw.line([(x, 0), (x, height)], fill=(255, 255, 255, 8))
for y_line in range(0, height, 100):
    draw.line([(0, y_line), (width, y_line)], fill=(255, 255, 255, 8))

# Draw a glowing center radial backdrop
glow_layer = Image.new("RGBA", (width, height), (0, 0, 0, 0))
glow_draw = ImageDraw.Draw(glow_layer)
center_x, center_y = width // 2, height // 2
for r in range(400, 0, -10):
    alpha = int(25 * (1 - r / 400))
    glow_draw.ellipse([center_x - r * 2, center_y - r, center_x + r * 2, center_y + r], fill=(0, 168, 107, alpha))
glow_layer = glow_layer.filter(ImageFilter.GaussianBlur(30))
img = Image.alpha_composite(img, glow_layer)
draw = ImageDraw.Draw(img)

# Overlay VE Logo if available
logo_path = r"c:\Users\asus\Documents\Company Project\images\ve_logo.png"
if os.path.exists(logo_path):
    logo = Image.open(logo_path).convert("RGBA")
    logo_size = 180
    logo = logo.resize((logo_size, logo_size), Image.Resampling.LANCZOS)
    img.paste(logo, (center_x - logo_size // 2, center_y - 230), logo)

# Load fonts
try:
    font_title = ImageFont.truetype("arialbd.ttf", 96)
    font_sub = ImageFont.truetype("arialbd.ttf", 36)
    font_tag = ImageFont.truetype("arialbd.ttf", 28)
except:
    font_title = ImageFont.load_default()
    font_sub = ImageFont.load_default()
    font_tag = ImageFont.load_default()

# Draw Text: Title
title_text = "VAJRESHWARI ENTERPRISES"
title_bbox = draw.textbbox((0, 0), title_text, font=font_title)
t_w = title_bbox[2] - title_bbox[0]
t_h = title_bbox[3] - title_bbox[1]

# Shadow
draw.text((center_x - t_w // 2 + 4, center_y - 10 + 4), title_text, font=font_title, fill=(0, 0, 0, 180))
# Text
draw.text((center_x - t_w // 2, center_y - 10), title_text, font=font_title, fill="#ffffff")

# Draw Text: Subtitle / Tagline
sub_text = "SERVING SINCE 2009  •  DRIVING SOLUTIONS, DELIVERING EXCELLENCE"
sub_bbox = draw.textbbox((0, 0), sub_text, font=font_sub)
s_w = sub_bbox[2] - sub_bbox[0]
draw.text((center_x - s_w // 2, center_y + 110), sub_text, font=font_sub, fill="#00c97f")

# Draw pill badge above
pill_text = "OFFICIAL BRANDING & CORPORATE OVERVIEW"
p_bbox = draw.textbbox((0, 0), pill_text, font=font_tag)
p_w = p_bbox[2] - p_bbox[0]
px, py = center_x - p_w // 2, center_y - 290
draw.rounded_rectangle([px - 20, py - 8, px + p_w + 20, py + 38], radius=20, fill=(0, 168, 107, 40), outline=(0, 201, 127, 120), width=2)
draw.text((px, py), pill_text, font=font_tag, fill="#ffffff")

# Save output image
out_path = r"c:\Users\asus\Documents\Company Project\images\about_hero_simple.png"
img.save(out_path, "PNG")
print("Saved banner to", out_path)
