# This program acts as meal price calculator. It will calculate the total price of the meal.
# Asking the user all the information.
child_meal = float(input("What is the price of a child's meal? "))
adult_meal = float(input("What is the price of an adult's meal? "))
children = int(input("How many children are there? "))
adults = int(input("How many adults are there? "))
sales_tax_rate = float(input("What is the sales tax rate? "))

# Computing  total price without sales tax
print("")
childs_total = (child_meal * children)
adults_total = (adult_meal * adults)

subtotal = (childs_total + adults_total)
print(f"Subtotal: ${subtotal:.2f} ")

# Computing what sales tax is.
sales_tax = (subtotal * sales_tax_rate / 100)
print(f"Sales Tax: ${sales_tax:.2f} ")

# Computing what the subtotal is with sales tax.
total = (subtotal + sales_tax)
print(f"Total: ${total:.2f} ")

# Computing tip and how much 15% tip would be if you add it.
tip = (total * .15 )
print(f"15% Tip Amount: ${tip:.2f} ")
with_tip = input("Do you want to pay a tip, yes or no? ")
tip_total = float(total + tip)

if with_tip == "yes":
    print(f"Total with tip is: ${tip_total:.2f} ")
elif with_tip == "no":
    print(f"Total: ${total:.2f} ")


# Computing what change is left.
print("")
payment = float(input("What is the payment amount? "))
change = (payment - total)
print(f"Change: ${change:.2f} ")

