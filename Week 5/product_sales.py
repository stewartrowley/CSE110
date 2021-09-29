# Get data from the user
num_product = int(input("How many products did you sell? "))
product_price = float(input("What is the price of the product? "))
commission_percent = float(input("What is your commission "))

# Calculate Commission 
# Convert to percentage:
commission_percent = commission_percent / 100
total_sale = num_product * product_price

commission_amount = total_sale * commission_percent

# Display results
print(f"The Total sales amount is ${total_sale:.2f} ")

if total_sale > 500:
    print("You recived a bonus!")
    print("It's a wonderful day!")
    commission_amount = commission_amount + 50
else:
    print("Thank you for your solid effort, unfortunatley.. your fired")

print(f"You made: ${commission_amount:.2f} ")
print("Thank you for using this wonderful program...")