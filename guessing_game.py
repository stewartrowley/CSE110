import random
keep_playing = "yes"
while keep_playing.lower() == "yes":
  magic_number = random.randint(1,20)
  guess = -1
  number_of_guesses = 0

  print("Please guess between 1 and 100! ")

  while guess != magic_number:
    guess = int(input("What is your guess? "))
    number_of_guesses = number_of_guesses + 1
    if guess > magic_number:
      print("Lower")
    elif guess < magic_number:
      print("Higher ") 

  print("Correct Answer!")
  print(f"You guessed {number_of_guesses} times!")

  keep_playing = input("Play Again? ")
  while keep_playing.lower() != "yes" and keep_playing.lower() != "no":
    keep_playing = input("Play Again? ")

print("thanks for playing! have a good day. ")
