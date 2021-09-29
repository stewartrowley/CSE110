# Input the values from the user.
fahrenheit = float(input("What is the temprature in Fahrenheit? "))
cel_temp = float(input("What is the tempature in Celsius "))

# Calculating the values.
celsius = (fahrenheit - 32) * (5/9)
fah_temp = (cel_temp * 9/5) + 32

# The output of the values.
print(f"The tempature in Celsius is {celsius:.1f} degrees.")
print(f"The tempature in Fahrenheit is {fah_temp:.1f} degrees.")
