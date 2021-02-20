"""
@author:  Aradhita Dasgupta      2nd year    CSE     Roll - 20

Print a month by importing calendar module.
"""

import calendar

year = int(input("Enter the year: "))
month = int(input("Enter the month no.: "))
    
try:
    print(calendar.month(year, month))
except:
    print("Wrong input.")
