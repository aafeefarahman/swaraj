from PIL import Image

# Open original logo
im = Image.open("logo.png").convert("RGBA")

# Auto-crop transparent borders
bbox = im.getbbox()
if bbox:
    im = im.crop(bbox)

# Icon sizes Chrome expects
sizes = [16, 32, 48, 128]

for size in sizes:
    resized = im.resize((size, size), Image.LANCZOS)
    filename = f"icon{size}.png"
    resized.save(filename)
    print(f"Saved {filename}")

print("✅ All icons generated without extra padding!")
