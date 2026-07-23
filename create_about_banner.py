import os
from PIL import Image, ImageDraw, ImageFont, ImageFilter

# Canvas dimensions (2400 x 750 4K quality)
width = 2400
height = 750

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
    draw.line([(x, 0), (x, height)], fill=(255, 255, 255, 6))
for y_line in range(0, height, 100):
    draw.line([(0, y_line), (width, y_line)], fill=(255, 255, 255, 6))

# Draw a glowing center radial backdrop
glow_layer = Image.new("RGBA", (width, height), (0, 0, 0, 0))
glow_draw = ImageDraw.Draw(glow_layer)
center_x, center_y = width // 2, height // 2
for r in range(350, 0, -10):
    alpha = int(22 * (1 - r / 350))
    glow_draw.ellipse([center_x - r * 2, center_y - r, center_x + r * 2, center_y + r], fill=(0, 168, 107, alpha))
glow_layer = glow_layer.filter(ImageFilter.GaussianBlur(25))
img = Image.alpha_composite(img, glow_layer)
draw = ImageDraw.Draw(img)

# Load font
try:
    font_title = ImageFont.truetype("arialbd.ttf", 110)
    font_sub = ImageFont.truetype("arialbd.ttf", 36)
except:
    font_title = ImageFont.load_default()
    font_sub = ImageFont.load_default()

# Draw Text: Only the Name "Vajreshwari Enterprises" + subtle subtext "Serving Since 2009"
title_text = "Vajreshwari Enterprises"
title_bbox = draw.textbbox((0, 0), title_text, font=font_title)
t_w = title_bbox[2] - title_bbox[0]
t_h = title_bbox[3] - title_bbox[1]

# Shadow
draw.text((center_x - t_w // 2 + 4, center_y - 45 + 4), title_text, font=font_title, fill=(0, 0, 0, 180))
# Text
draw.text((center_x - t_w // 2, center_y - 45), title_text, font=font_title, fill="#ffffff")

# Subtext "Serving Since 2009"
sub_text = "SERVING SINCE 2009"
sub_bbox = draw.textbbox((0, 0), sub_text, font=font_sub)
s_w = sub_bbox[2] - sub_bbox[0]
draw.text((center_x - s_w // 2, center_y + 85), sub_text, font=font_sub, fill="#00c97f")

# Save output image
out_path = r"c:\Users\asus\Documents\Company Project\images\about_hero_simple.png"
img.save(out_path, "PNG")
print("Saved clean banner to", out_path)
