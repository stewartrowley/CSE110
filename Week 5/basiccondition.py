# input the values 
first = int(input("What is the first number? "))
second = int(input("What is the second number? "))
print()

# Determine what is greater or not
if first > second:
    print("The first number is greater")
elif first < second:
    print("The first number is not greater")

if first == second:
    print("The numbers  are equal")
elif first != second:
    print("The numbers are not equal")

if first < second:
    print("The second number is greater")
elif first > second:
    print("The second number is not greater")
print()

# Determine your values
animal = input("What is your favorite animal? ")
if animal == "giraffe":
    print("That one is not my favorite.")
elif animal == "bear":
    print("That's my favorite animal too")
else:
    print("Those are weird animals.")

