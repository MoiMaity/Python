"""
@author:  Aradhita Dasgupta      2nd year    CSE     Roll - 20

Print the name of days in a week.
"""

import calendar

for i in range(7):
    print("Day", str(i+1)+":", str(calendar.day_name[i]))
