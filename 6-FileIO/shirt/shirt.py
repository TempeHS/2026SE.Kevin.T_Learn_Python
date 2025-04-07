import sys
from PIL import Image, ImageOps

if len(sys.argv) > 3:
    print("Too many arguments")
    sys.exit()
elif len(sys.argv) < 3:
    print("Too few arguments")
    sys.exit()

try:
    open(sys.argv[1])
except FileNotFoundError:
    print("File not found")
    sys.exit()

image = Image.open(sys.argv[1])
overlay = Image.open("took.png")
size = image.size

overlay = ImageOps.fit(overlay, image.size)
image.paste(overlay, overlay)
image.save(sys.argv[2])
