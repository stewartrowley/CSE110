
# Asking the user information
large_loan = int(input("How large is the loan? "))
credit_score = int(input("How good is your credit history? "))
income = int(input("How high is your income? "))
down_payment = int(input("How large is your down payment? "))

if large_loan >= 5:
    if credit_score >= 7 and income >= 7:
        loan = True
    elif credit_score >= 7 or income >= 7:
        if down_payment >= 5:
            loan = True
        else:
            loan = False
    else:
        loan = False
elif large_loan < 5:
    if credit_score < 4:
        loan = False
    else:
        if income >= 7 or down_payment >= 7:
            loan = True
        elif income >= 4 and down_payment >= 4:
            loan = True
        else:
            loan = False

# Displaying the results
if loan:
    print("The decision is a yes")
else:
    print("The decision is no")

    

