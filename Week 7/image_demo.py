from PIL import Image

# file_to_open = input("Which file would you like to open? ")

shuttle = Image.open("spaceshuttle.jpg")
earth = Image.open("earth.jpg")

shuttle_pixels = shuttle.load()
earth_pixels = earth.load()


# red = 255
# green = 0
# blue = 255
for x in range(0, 800):
    for y in range(0, 600):
        
        (red, green, blue) = earth_pixels[x, y]
        if red < 130 and green > 0 and blue < 130:
            shuttle_pixels[x, y] = (red, green, blue)
        else: 
            earth_pixels[x, y] = (red, green, blue)





shuttle.show()
shuttle.save("spaceshuttle_earth.jpg")