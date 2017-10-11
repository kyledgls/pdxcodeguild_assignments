from PIL import Image
import colorsys

img = Image.open("daysix/Lenna.png") # must be in same folder
width, height = img.size
pixels = img.load()

for i in range(width):
    for j in range(height):
        r, g, b = pixels[i, j]
        h, s, v = colorsys.rgb_to_hsv(r / 255, g / 255, b / 255)
        r = int(.1*r)
        g = int(.1*g)
        b = int(.1*b)

        pixels[i, j] = (r, g, b)

img.show()