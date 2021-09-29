import math

def compute_area_square(side):
  area = side * side
  return area
  
def compute_area_circle(radius):
  area = math.pi * radius * radius
  return area

def compute_area_rectangle(length, width):
  area = length * width
  return area


shape_list = ["rectangle", "circle", "square", "quit"]
shape = ""

while shape != "quit":
  shape = input("Which shape do you want to know the area of? ").lower()
  while shape not in shape_list:
    shape = input("Invalid input\nWhich shape do you want to know the area of? ")
    
  if shape == "square":
    side= float(input("What is the length of the side? "))
    area = compute_area_square(side)
      
  elif shape == "circle":
    radius = float(input("What is the radius for the circle ? "))
    area = compute_area_circle(radius)

  elif shape == "rectangle":
    width = float(input("What is the width of the rectangle? "))
    length = float(input("What is the length of the rectangle? "))
    area = compute_area_rectangle(width, length)
      
    
  print(f"The area of the {shape} equals {area:.2f} units squared")
  
  shape = input("\nWould you like to find the area of another shape (quit/continue)? ").lower()