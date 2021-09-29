
# Function that run the equations and convertions
def wind_chill(temperature):
    t = user_temperature
    chill = 35.74 + 0.6215 * t - 35.75 * (v ** 0.16) + 0.4275 * t * (v ** 0.16)
    return chill

def temp_convertion(convertion):
    f = (t * 9 / 5) + 32
    chill = 35.74 + 0.6215 * f - 35.75 * (v ** 0.16) + 0.4275 * f * (v ** 0.16)
    return chill

user_temperature = float(input("What is the temperature? "))
user_type = input("Fahrenheit or Celsius (F/C)? ")
t = user_temperature

# The loop that runs through this range of numbers 
for v in (range(5, 65, 5)):
    if user_type == "F":
        user_chill = wind_chill(user_temperature)
        print(f"At temperature {t}F, and wind speed {v} mph, the windchill is: {user_chill:.2f}F")
    elif user_type == "C":
        user_convertion = temp_convertion(user_temperature)
        print(f"At temperature {t}F, and wind speed {v} mph, the windchill is: {user_convertion:.2f}F")




