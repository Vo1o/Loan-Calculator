# Loan-Calculator
Loan calculator written in python
You can run your loan calculator via command line like this:
python creditcalc.py

Using command-line arguments you can run your program this way:
python creditcalc.py --type=diff --principal=1000000 --periods=10 --interest=10

--type indicates the type of payment: "annuity" or "diff" (differentiated). If --type is specified neither as "annuity" nor as "diff" or not specified at all, show the error message.
> python creditcalc.py --principal=1000000 --periods=60 --interest=10
Incorrect parameters

--payment is the monthly payment amount. For --type=diff, the payment is different each month, so we can't calculate months or principal, therefore a combination with --payment is invalid, too:
> python creditcalc.py --type=diff --principal=1000000 --interest=10 --payment=100000
Incorrect parameters

--principal is used for calculations of both types of payment. You can get its value if you know the interest, annuity payment, and number of months.
--periods denotes the number of months needed to repay the loan. It's calculated based on the interest, annuity payment, and principal.
--interest is specified without a percent sign. Note that it can accept a floating-point value. Our loan calculator can't calculate the interest, so it must always be provided. 

These parameters are incorrect because --interest is missing:
> python creditcalc.py --type=annuity --principal=100000 --payment=10400 --periods=8
Incorrect parameters

Examples:
> python creditcalc.py --type=diff --principal=1000000 --periods=10 --interest=10
Month 1: payment is 108334
Month 2: payment is 107500
Month 3: payment is 106667
Month 4: payment is 105834
Month 5: payment is 105000
Month 6: payment is 104167
Month 7: payment is 103334
Month 8: payment is 102500
Month 9: payment is 101667
Month 10: payment is 100834
Overpayment = 45837

Example 2: calculate the annuity payment for a 60-month (5-year) loan with a principal amount of 1,000,000 at 10% interest
> python creditcalc.py --type=annuity --principal=1000000 --periods=60 --interest=10
Your annuity payment = 21248!
Overpayment = 274880

Example 3: fewer than four arguments are given
> python creditcalc.py --type=diff --principal=1000000 --payment=104000
Incorrect parameters.

Example 4: calculate differentiated payments given a principal of 500,000 over 8 months at an interest rate of 7.8%
> python creditcalc.py --type=diff --principal=500000 --periods=8 --interest=7.8
Month 1: payment is 65750
Month 2: payment is 65344
Month 3: payment is 64938
Month 4: payment is 64532
Month 5: payment is 64125
Month 6: payment is 63719
Month 7: payment is 63313
Month 8: payment is 62907
Overpayment = 14628

Example 5: calculate the principal for a user paying 8,722 per month for 120 months (10 years) at 5.6% interest
> python creditcalc.py --type=annuity --payment=8722 --periods=120 --interest=5.6
Your loan principal = 800018!
Overpayment = 246622

Example 6: calculate how long it will take to repay a loan with 500,000 principal, monthly payment of 23,000, and 7.8% interest
> python creditcalc.py --type=annuity --principal=500000 --payment=23000 --interest=7.8
It will take 2 years to repay this loan!
Overpayment = 52000
