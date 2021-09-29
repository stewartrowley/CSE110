positive_num = float(input("Please type a positive number: "))

while positive_num <= 0:
    print("Sorry, that is a negative number. Please try again.")
    positive_num = float(input("Please type a positive number: "))

print(f"The number is: {positive_num}")

candy_piece = ""

while candy_piece.lower() != "yes":
    candy_piece = input("May I have a piece of candy ")

print(f"Thank you.")