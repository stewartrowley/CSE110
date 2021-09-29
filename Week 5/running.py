conditions = input("What are the current world conditions (monsoon, tornado, volcano, normal)? ")
conditions = conditions.lower()

#if conditions == "tornado" or conditions == "volcano":
#if conditions in["tornado", "volcano", "earthquake"]:
if conditions =="tornado":
    print("Do not go running")
elif conditions == "volcano":
    print("Run really fast!")
elif conditions == "normal":
    temperature = float(input("What is the tempature? "))
    
    if temperature < 15:
        print("Don't go runnning")
    elif temperature < 30:
        print("It's ok, but wear a jacket")
    elif temperature > 90:
        print("Too hot! Stay inside.")
else:
    print("It complicated!")

