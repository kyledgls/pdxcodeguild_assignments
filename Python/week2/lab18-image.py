from PIL import Image
import colorsys

img = Image.open("Lenna.png") # must be in same folder
width, height = img.size
pixels = img.load()

for i in range(width):
    for j in range(height):
        r, g, b = pixels[i, j]
        h, s, v = colorsys.rgb_to_hsv(r / 255, g / 255, b / 255)
        r = int(255*r)
        g = int(255*g)
        b = int(255*b)

        pixels[i, j] = (r, g, b)

img.show()