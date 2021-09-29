# The begining of the game!
print("Welcome to the the adventure game of your life!!")
print()

#The two main decisions!
print("There are two different themes you can pick for this game, FARY TALES or SCIENCE FICTION! ")
theme = input("What genre do you pick? ")
print()

# Start of the if statements
if theme == "fary tales":
    print("fary tales!! Wonderful choice! Prepare your mind for a dream to come true.")
    fary_tales = input("Once upon a time a person is walking in the woods. That person is a PRINCE or PRINCESS? ")
    fary_tales = fary_tales.lower()

    # The prince's jourey along the way.
    if fary_tales == "prince":
        print("As the prince was walking into the forest back to the castle. He met a person who was holding gold coins and a nice sword.")
        print("Better then the sword he had.The man said to him which one do you want it is your to keep." )
        items = input("Which do you take, SWORD or GOLD COINS? ")
        items = items.lower()

        if items == "gold coins":
            print("As you are walking back to the castle you run into a bridge, but there are trolls.")
            print("who are guarding the bridge. They make a threat to you if you don't pay us some gold coins,")
            print("to get accross then we will kill you.")
            bridge_threat = input("Do you FIGHT or PAY or SNEAK by ")
            bridge_threat = bridge_threat.lower()
            
            if bridge_threat == "fight":
                print("As you fight the trolls, without the powerful sword, that the man had,")
                print("on the trail. You lose the fight and die from being stabbed from the trolls.") 
                print("Game Over!")
            elif bridge_threat == "pay":
                print("From paying the trolls you were able to cross, therefore making it back into to the castle and getting married to the princess!")
                print("You lived happily ever after!!")
                # Determining the wealth if statements
                if bridge_threat == "pay":
                    age = int(input("How old are you as a prince or princess? in this game you can be between 18-26 years old. "))
                    print("Your age determines how much gold your kingdom has if you lived happily ever after.")
                    if age >= 18 and age <= 20:
                        print("You have 1 million gold coins")
                    elif age > 20 and age <= 22:
                        print("You have 2 million gold coins")
                    elif age > 22 and age <= 24:
                        print("You have 3 million gold coins")
                    elif age > 24 and age <= 26:
                        print("You have 4 million gold coins")
                    else:
                        print("Your age is invalid.") 
            elif bridge_threat.lower() == "sneak":
                print("Unforunatly, you try to sneak by but in doing so, they catch you and you die. Game Over!!")

        elif items == "sword":
            print("You take the sword and as you are walking to the castle, you come across a bridge you have to cross.")
            print("There are some trolls protecting it. they don't coorperate with you. so, you end up taking them out")
            print("with your powerful sword you got from the person. While you were in the process of taking them out.")
            print("From the battle you ended up getting a small cut from one of there poisnous sword. You start hurting from the poison")
            print("With the magic poison you question if you can make it back to the castle. Will you last long enough.")
            print("Below the bridge, the water has magical healing property's")
            endurance = input("Do you believe you can make it to the castle before you die from the poison or do you grab the healing water to heal yourself? HEALING WATER or PUSH THROUGH? ")
            endurance = endurance.lower()

            if endurance == "push through":
                print("You move on and as you get close to the castle, you collapse on the ground and die. Game Over!!")
            elif endurance == "healing water":
                print("You go down to the water and grab some in your pouch and pour it onto the cut and you are healed. You continue your")
                print("journey back to the castle and get married to the princess. You lived happily ever after!!")
                # Determining the wealth if statements
                if endurance == "healing water":
                    age = int(input("How old are you as a prince or princess? in this game you can be between 18-26 years old. "))
                    print("Your age determines how much gold your kingdom has if you lived happily ever after.")
                    if age >= 18 and age <= 20:
                        print("You have 1 million gold coins")
                    elif age > 20 and age <= 22:
                        print("You have 2 million gold coins")
                    elif age > 22 and age <= 24:
                        print("You have 3 million gold coins")
                    elif age > 24 and age <= 26:
                        print("You have 4 million gold coins")
                    else:
                        print("Your age is invalid.") 
    
    elif fary_tales == "princess":
        print("As your riding in the carriage to the castle, your carriage wheel falls off. putting you to a complete stop.")
        print("A man saw that, and came up to you to offer his horse or to fix the carriage")  
        transportation = input("Which do you pick HORSE or WHEEL? ")
        transportation = transportation.lower()
        
        if transportation == "horse":
            print("He gives you the horse. The horse has great speed but as you get closer to the castle you get lost.")
            print("Do you go back and get help by the nearest small town or do you continue on and hope you make it?")
            directions = input("SMALL TOWN or KEEP RIDING? ")
            directions = directions.lower()

            if directions == "small town":
                print("As you make it back to the small town you stumble accross someone who has a map and he gives it to you.")
                print("You take it and you are able to find your way to back to the castle.")
                print("You marry the prince and live happily ever after!!")
                # Determining the wealth if statements
                if directions == "small town":
                    age = int(input("How old are you as a prince or princess? in this game you can be between 18-26 years old. "))
                    print("Your age determines how much gold your kingdom has if you lived happily ever after.")
                    if age >= 18 and age <= 20:
                        print("You have 1 million gold coins")
                    elif age > 20 and age <= 22:
                        print("You have 2 million gold coins")
                    elif age > 22 and age <= 24:
                        print("You have 3 million gold coins")
                    elif age > 24 and age <= 26:
                        print("You have 4 million gold coins")
                    else:
                        print("Your age is invalid.") 
            
            elif directions == "keep riding":
                print("As you continue on, you become so lost. You don't know where your at. All the sudden a troll comes out of nowhere and you die.")
                print("Game Over!!!")

        elif transportation == "wheel":
            print("As you get the wheel and fix the carriage. You follow the road and all the sudden bandits attack your wagon.")
            print("The bandits want the gold coins that is sitting in your carriage.")
            print("Do you give them the gold coins in the carriage or you deny them?")
            cost_threat = input("GOLD COINS or DENY THEM? ")
            cost_threat = cost_threat.lower()

            if cost_threat == "gold coins":
                print("You give them the gold coins and you make back to the castle and married the prince!")
                print("You lived Happily Ever After!!!")
                # Determining the wealth if statements
                if cost_threat == "gold coins":
                    age = int(input("How old are you as a prince or princess? in this game you can be between 18-26 years old. "))
                    print("Your age determines how much gold your kingdom has if you lived happily ever after.")
                    if age >= 18 and age <= 20:
                        print("You have 1 million gold coins")
                    elif age > 20 and age <= 22:
                        print("You have 2 million gold coins")
                    elif age > 22 and age <= 24:
                        print("You have 3 million gold coins")
                    elif age > 24 and age <= 26:
                        print("You have 4 million gold coins")
                    else:
                        print("Your age is invalid.") 
            elif cost_threat == "deny them":
                print("The the thiefs stab you and then take the gold coins. Game Over!!")
#Science fiction theme      
elif theme == "science fiction":
    print("science fiction!! Crazy choice! Prepare your mind with thinking of how deep space is and where are you in space?")
    print("You start out in space but while your in space. Your spaceship starts to have issues. So where you are at,")
    print("you look around and see a near by planet. You have never been there before. You fly down to there and see it is inhabited by people.")
    print("As you land your spaceship, a part on it breaks. A part that is important and will cause you to have to stay and fix it.")
    print("Until you fix it, you will not be able to leave the planet. As you walk into the nearby town. Your in search of someone to help you fix it.")
    print("As you get this person, you don't see the bigger picture. This town is being runned by evil driods. This person is wanted by them because he is trying to destroy the driods and it's leader.")
    print("So, the people can be free. He is wanted because of that, he makes you a deal if you can help him overthrow the leader of the driods then he will help you get off the planet.")
    help_planet = input("Do you HELP or NOT? ")

    if help_planet == "help":
        print("By helping him, he gives you a light saber and tells you how to use it. He tells you the plan to sneek into the where the driod leader is.")
        print("He tells you directions of the driod leader and to meet him there. He also tells you to use the lightsaber to take out the driods.")
        print("You get there first but he told you to wait and to not aproach the leader until he is there.")
        print("What do you do, folow him or not")
        obey = input("FOLLOW HIM or DON'T? ")

        if obey == "follow him":
            print("You follow him and wait there for him to come. He gets there and you are able to defeat the leader together!")
            print("By defeating the leader the town goes back to normal and the guy helps you off the planet. You Win!")
        elif obey == "don't":
            print("By not waiting the leader destroys you and you lose. Game Over!!")
        
    elif help_planet == "not":
        print("You lose the game! You are stuck on the island forever!")

else:
    print("You are out of the adventure game and will not proceed forward. Check your spelling.") 

     
    
