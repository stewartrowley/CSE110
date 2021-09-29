def compute_tithing(income):
    tithing = income / 10
    return tithing

user_income = float(input("Type in income: "))

user_tithing = compute_tithing(user_income)

print(f"Tithing was ${user_tithing:.2f}")