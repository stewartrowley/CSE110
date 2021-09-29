names = []

new_names = None

while new_names != "end":
    new_names = input("Type the name of a friend: ")
    

    if new_names != "end":
        names.append(new_names)

print()
print("Your friends are: ")

for name in names:
    print(name)
