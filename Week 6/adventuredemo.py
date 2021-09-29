print("Welcome to the adventure")

fork_in_road = input("You come to a fork in the road. Do you want to go LEFT or RIGHT? ")

if fork_in_road.lower() == "left":
    print("You went left")
    print("You came upon a giant potato.")
    potato_choice = input("Do you want to PUNCH it or EAT it? ")

    if potato_choice.lower() == "eat":
        print("It was delicious")

        drink_choice = ("Your stomach started rumbling.. Do you want to DRINK some water or NOT? ")
        
        if drink_choice.lower():
            print("it feels better..")

elif fork_in_road.lower() == "right":
    print("You went right")
else:
    print("I didn't quite get that..")


