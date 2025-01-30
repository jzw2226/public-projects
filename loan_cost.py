#Ask the user and record the amount of money they borrowed, the annual interest rate, and the number of payments to be made

loan = float(input("Please enter the amount of money you borrowed: $"))
annualInterest = float(input("Please enter the annual interest rate: "))
numPayments = float(input("Please enter the number of payments to be made: "))

#Calculate and record the user's monthly interest and payment amount using the equation given

monthlyInterest = annualInterest / 12
payment = (loan * monthlyInterest)/(1 - (1 + monthlyInterest) ** (-numPayments))

#Multiply the calculated monthly payment by the number of payments to be made and record the result as the total amount the user will pay

totalPayment = payment * numPayments

#Subtract the loaned amount from the total amount the user will pay and record the result as the cost of the loan

cost = totalPayment - loan

#Inform the user of the amount they loaned, the annual interest rate, the number of months they wish to use to pay the loan off, the monthly payment amount, the total paid amount, and the cost of the loan.

print(f"A loan of ${loan:.2f} with an annual interest of {annualInterest:.2f} paid off over {numPayments:.0f} months will have monthly payments of ${payment:.2f}.\nIn total, you will pay ${totalPayment:.2f}, making the cost of your loan ${cost:.2f}.")