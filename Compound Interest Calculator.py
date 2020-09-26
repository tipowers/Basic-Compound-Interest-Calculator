# This program will compute the amount earned on an account after x amount of years using principal,
# annual interest, and compound interest rate.

print('\nThis program will calculate the amount earned on an account using compound interest!\n')
# Get the initial principal amount.
principal_amount = float(input('What is the principal amount originally deposited into the account? \n'))

# Get the initial annual interest using numbers between 0 and 100.
annual_interest = float(input('What is the annual interest rate of the account? Enter as a percentage. Ex. 2% would be entered as 2. '))

# Get the compund rate by asking how often the user wants interest to be compunded in a year.
compound_rate = int(input('How many times per year do you want the interest compounded? Ex. quarterly enter 4. '))

# Compute the annual interest rate by taking the user input annual interest and dividing by 100.
annual_interest = annual_interest / 100

# Get how many years user wants account to be open.
years_of_account = int(input('How many years will the account be open to earn interest? '))

# Compute end total by using the formula A = P*(1 + r/n)**nt
end_total = principal_amount * (1 + annual_interest/compound_rate)**(compound_rate * years_of_account)

# Output the end total.  Format answer to 2 decimal places.
print ('\nThe balance of the account after ', years_of_account, ' years is: $', format(end_total, ',.2f'), sep = '')

print ('\nAuthored by: Tim Powers')

