# program where user inputs what is in there cart and total
print("Welcome to the shopping Cart Program!")

choice = -1
order_list = []
names = []
costs = []
name = None

# keep asking as long as they don't choose option 6

while choice != 6:
    print("")
    print("Please select one of the following:")
    print("1. Add item")
    print("2. View Cart")
    print("3. Remove item")
    print("4. Replace item")
    print("5. Compute total")
    print("6. Quit")

    choice = int(input("Please enter an action: "))
    
    # the different choices you can select through a big if statement 
    if choice == 1:
        name = input("What item would you like to add? ")
        name = name.capitalize()
        cost = float(input(f"What is the price of '{name}'? "))
        print(f"'{name}' has been added to the cart.")
        names.append(name)
        costs.append(cost)

    elif choice == 2:
        print("\nThe contents of the shopping cart are:")
        for i in range(len(names)):
            print(f"{i+1}. {names[i]} - ${costs[i]:.2f}")           
            
    elif choice == 3:
        for i in range(len(names)):
            print(f"{i+1}. {names[i]} - ${costs[i]:.2f}")  
        remove_item = int(input("What item do you want to remove? (type number) "))
        names.pop(remove_item - 1)
        costs.pop(remove_item - 1)
        print("Item removed from cart.")
        for i in range(len(names)):
            print(f"{i+1}. {names[i]} - ${costs[i]:.2f}")  
    
    elif choice == 4:
        for i in range(len(names)):
            print(f"{i+1}. {names[i]} - ${costs[i]:.2f}")  
        item_to_replace = int(input("What item do you want to replace? (type number) "))
        index_to_replace = item_to_replace - 1

        name = input("What is the new name? ")
        name = name.capitalize()
        cost = float(input("What is the new price? "))

        # This will replace the current spot 
        names[index_to_replace] = name
        costs[index_to_replace] = cost

    elif choice == 5:
        total = sum(costs)
        print(f"The total price is ${total:.2f}")

        taxes = total * .06
        total_with_taxes = taxes + total
        print(f"The total price with taxes is ${total_with_taxes:.2f}")

print("Thank you. Goodbye.")

     


