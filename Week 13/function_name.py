def display_name(message):
    print(message)
def display_uppercase(message):
    new_uppercase = message.upper()
    print(new_uppercase)
def display_lowercase(message):
    new_lowercase = message.lower()
    print(new_lowercase)

user_message = input("What is your message? ")

display_name(user_message)
display_uppercase(user_message)
display_lowercase(user_message)