"""
paycheck.py
Calculates a user's paycheck based on information entered by the user:
1. Hourly Rate
2. Hours Worked
3. Overtime Rate
"""

# Import Decimal Library
from decimal import Decimal

# Converts input string to Decimal
pay_rate = Decimal(input("What's your hourly rate in US dollars?\n"))
hours = Decimal(input("How many hours did you work this week?\n"))

# Calculates overtime pay
def calcPay():
    if hours > 40:
        regular_hours = 40
        overtime_rate = Decimal(input("What is your overtime rate?\n"))
        overtime_hours = hours - regular_hours
        overtime_pay = overtime_hours * pay_rate * overtime_rate
        # Adds overtime payrate to paycheck
        paycheck = (pay_rate * regular_hours) + overtime_pay
        # Rounds paycheck to two decimal points
        paycheck = round(paycheck, 2)
        print("This week you'll be paid: $%s" % (paycheck))
    # Calculates regular pay
    else:
        paycheck = pay_rate * hours
        # Rounds paycheck to two decimal points
        paycheck = round(paycheck, 2)
        print("This week you'll be paid: $%s" % (paycheck))
