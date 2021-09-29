
from PIL import Image

image_snowscape = Image.open("snowscape.jpg")

width, height = image_snowscape.size
# print(f"The width is {width} ")

ss_pixels = image_snowscape.load()
print(ss_pixels[8, 16])

x = 8
while x < 600:
    ss_pixels[x, 16] = (200, 0, 200)
    x = x + 1

 s_pixels = image_snowscape.load()
 print(s_pixels[102, 145])

y = 145
while y < 600:
    s_pixels[102, y] = (0, 240, 230)
    y = y + 1

   
image_snowscape.show()