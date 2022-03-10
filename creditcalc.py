import argparse
import math

parser = argparse.ArgumentParser(description="Calculate the loan")
parser.add_argument("--type_", type=str, help="Annuity or Diff only")
parser.add_argument("--principal", type=int, help="Loan Principal")
parser.add_argument("--payment", type=int, help="Monthly Payment")
parser.add_argument("--interest", type=float, help="Loan Interest")
parser.add_argument("--periods", type=int, help="Number of periods")

args = parser.parse_args()

if args.type_ == "diff" and args.principal and args.periods and args.interest:
    nom_rate = (args.interest / 100) / 12
    total = 0
    for m in range(1, args.periods + 1):
        d = math.ceil(args.principal / args.periods + nom_rate * (args.principal - (args.principal * (m - 1)) / args.periods))
        print(f"Month {m}: payment is {d}")
        total += d
    print()
    print(f"Overpayment = {total - args.principal}")

if args.type_ == "annuity" and args.payment and args.periods and args.interest:
    nom_rate = (args.interest / 100) / 12
    z = (1 + nom_rate) ** args.periods
    loan_principal = args.payment / ((nom_rate * z) / (z - 1))
    loan_principal_ = math.ceil(loan_principal)
    print(f"Your loan principal = {loan_principal_}!")
    over_pay = args.payment * args.periods - loan_principal_
    print(f"Overpayment = {over_pay}")
elif args.type_ == "annuity" and args.principal and args.periods and args.interest:
    nom_rate = (args.interest / 100) / 12
    z = (1 + nom_rate) ** args.periods
    annuity_payment = args.principal * ((nom_rate * z) / (z - 1))
    m_payment = math.ceil(annuity_payment)
    print("Your monthly payment = " + str(m_payment) + "!")
    over_pay = m_payment * args.periods - args.principal
    print(f"Overpayment = {over_pay}")
elif args.type_ == "annuity" and args.principal and args.payment and args.interest:
    nom_rate = (args.interest / 100) / 12
    xy = math.log(args.payment / (args.payment - nom_rate * args.principal), 1 + nom_rate)
    xy_ = math.ceil(xy)  # Number of months
    yr = xy_ // 12  # Years
    mths = xy_ % 12  # Months
    if xy_ == 1:
        print(f'It will take {xy_} month to repay this loan!')
    elif 1 < xy_ < 12:
        print(f'It will take {xy_} months to repay this loan!')
    elif xy_ == 12:
        print(f'It will take {yr} year to repay this loan!')
    elif xy_ % 12 == 0 and yr > 1:
        print(f'It will take {yr} years to repay this loan!')
    elif yr == 1 and mths == 1:
        print(f'It will take {yr} year and {mths} month to repay this loan!')
    elif yr == 1 and mths > 1:
        print(f'It will take {yr} year and {mths} months to repay this loan!')
    elif yr > 1 and mths == 1:
        print(f'It will take {yr} years and {mths} month to repay this loan!')
    else:
        print(f'It will take {yr} years and {mths} months to repay this loan!')
    over_pay = args.payment * xy_ - args.principal
    print(f"Overpayment = {over_pay}")
else:
    print("Incorrect parameters.")
