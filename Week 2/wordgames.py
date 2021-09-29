print("Please enter the following:\n")

word1 = input("adjective: ")
word1 = word1.lower()
word2 = input("animal: ")
word2 = word2.lower()
word3 = input("verb: ")
word3 = word3.lower()
word4 = input("exclamation: ")
word4 = word4.capitalize()
word5 = input("verb: ")
word5 = word5.lower()
word6 = input("verb: ")
word6 = word6.lower()

print("Your story is:\n")

print("The other day, I was really in trouble. It all started when I saw a very")
print(f'{word1} {word2} {word3} down the hallway. "{word4}!" I yelled. But all')
print(f"I could think to do was to {word5} over and over. Miraculously,")
print(f"that caused it to stop, but not before it tried to {word6}")
print(f"right in front of my family.\n")
print(f"Picture this in your {word1} head")
print(f"How do you feel about this story?")

summary = input("Please enter your thoughts about the story here: ")

