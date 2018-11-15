"""
paycheck.py
Calculates a user's weekly paycheck based on information entered by the user:
1. Hourly Rate
2. Hours Worked
3. Overtime Rate
"""

# Import decimal library
from decimal import Decimal

pay_rate = input("What's your hourly rate in US dollars?\n")
hours = input("How many hours did you work this week?\n")
overtime_rate = input("What is your overtime rate?\n")

try:
    # Converts input string to decimal
    pay_rate = Decimal(pay_rate)
    hours = Decimal(hours)
    overtime_rate = Decimal(overtime_rate)

    # 40 hour work week
    regular_hours = 40

    # Defined two separate functions to calculate regular and overtime pay
    def regularPay():
        paycheck = pay_rate * hours
        print(paycheck)
        return paycheck

    def overtimePay():
        overtime_hours = hours - regular_hours
        overtime_pay = overtime_hours * pay_rate * overtime_rate
        # Adds overtime pay to paycheck
        overtime_check = (pay_rate * regular_hours) + overtime_pay
        # Rounds paycheck to two decimal points
        overtime_check = round(overtime_check, 2)
        print(overtime_check)
        return overtime_check

    if hours <= regular_hours:
        regularPay()
    else:
        overtimePay()

except:
    # Prints when user enters a non-numerical input
    print("Please enter a number unless you're prompted otherwise.")