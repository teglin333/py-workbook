# Compute and display the saving account balance after
# 1, 2, and 3 years, accounting for a 4 percent interest rate per year

interest_rate = 0.04
future_year = 2026
current_year = 2023

def compute_compound_interest(balance):
    return balance + (balance * interest_rate)

account_balance = float(input('Enter the savings account balance in %d: $' % current_year))

current_year += 1

while current_year <= future_year:
    account_balance = compute_compound_interest(account_balance)
    print ("In %d, balance will be: $%.2f." % (current_year, account_balance))
    current_year += 1