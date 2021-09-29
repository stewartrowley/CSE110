# price = input("how much did you pay? ")

# price = float(price)
# if price >= 1.00:
#     tax =.07
#     print(f"Tax rate is: {tax} ")
# else:
#     tax = 0
#     print(f"Tax rate is: {tax} ")

# country = input("Enter the name of your home country: ")
# if country.lower() == "united states":
#     print("So you must like hockey!")
# else:
#     print("You are not from United States")

country = input("What country do you live in? ")

if country.lower() == "canada":
    province = input("What province/state do you live in? ")
    if province in("Alberta",\
        "Nunavut", "Yukon"):
        tax = 0.05
    elif province == "Ontario":
        tax = 0.13
    else:
        tax = 0.15
        
else:
    tax = 0.0
print(tax)