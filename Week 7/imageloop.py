# This line imports or includes the library we will need
from PIL import Image

# This line opens the image and loads it into a variable called "image_original"
image_snowscape = Image.open("snowscape.jpg")
image_penguin = Image.open("penguin.jpg")
# This line attrmpts to open a new window to display the image.
# image_snowscape.show()

# print(image_snowscape.size)
# print(image_snowscape.format)



pixels_snowscape = image_snowscape.load()
pixels_penguin = image_penguin.load()




for y in range(0, 600):
    for x in range(0, 800):
        (r, g, b) = pixels_penguin[x, y]
        (r, g, b) = pixels_snowscape[x, y]

        if r > 140 and g < 0 and b > 150:
            pixels_snowscape[x, y] = (r, g, b)
        elif r < 230 and g > 120 and b < 2232:
            pixels_penguin[x, y] = (r, g, b)
        
        # elif r > g and b > g:
        #     (r, g, b) = image_penguin[x, y]

        #     image_penguin[x, y] = (r, g, b)

# image_combined = Image.new("RGB", image_snowscape.size)
# pixels_new = image_combined.load()

#image_combined.show()
image_snowscape.show()
#image_penguin.show()
#image_snowscape.save("snowscape_blue_square.jpg")


# width, height = image_original.size

# pixels_original = image_original.load()

# r, g, b = pixels_original[250, 100, 250]


# # Don't forget to use parentheses around your (r, g, b)
# pixels_original[250, 100, 250] = (r, g, b)


