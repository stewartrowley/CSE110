choice = -1
order_list = []

# keep asking as long as they don't say "quit"

while choice != 5:
    print("Here are the menu options:")
    print("1. Eggs")
    print("2. Chicken")
    print("3. Carrots")
    print("4. Tv Dinner")
    print("5. Finsih order")

    choice = int(input("Please make a choice: "))

    if choice == 1:
        order_list.append("Eggs")
    elif choice == 2:
        order_list.append("Chicken")
    elif choice == 3:
        order_list.append("Carrots")
    elif choice == 4:
        order_list.append("TV Dinner")

    order_list.append(choice)

print("Thank you for your order")
print("You have ordered:")

for item in order_list:
    print(f" {item}")


# value < largest should be: value > largest
# value should of start at a large number

# movies.pop(3)