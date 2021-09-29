list_accounts = []
list_balance = []
account_name = "None"

print("Enter the names and balances of bank accounts (type: 'quit' when done")
while account_name != "quit":
    account_name = input("What is the name of the account? ")
    account_name = account_name.lower()
    if account_name != "quit":
      account_balance = float(input("what is the balance? "))
      list_accounts.append(account_name)
      list_balance.append(account_balance)

print("\nAccount Information:")
for x in range(len(list_accounts)):
  account = list_accounts[x]
  balance = list_balance[x]
  print(f"{x}. {account} - ${balance:.2f}")
  
total = sum(list_balance)
print(f"\nTotal: ${total:.2f}")
average = total / (len(list_balance))
print(f"Average: ${average:.2f}")

largest_account = list_balance.index(max(list_balance))
print(f"Highest Balance: {list_accounts[largest_account]} - ${list_balance[largest_account]:.2f}")

update_question = input("Would you like to update an account? ")
if update_question.lower() == "yes":
  account_index = int(input("What is the index of the account you wish to update? "))
  new_amount = float(input("What is the new amount? "))
  list_balance[account_index] = new_amount
  
print("\nAccount Information:")
for x in range(len(list_accounts)):
  account = list_accounts[x]
  balance = list_balance[x]
  print(f"{x}. {account} - ${balance:.2f}")