"""
@author:  Aradhita Dasgupta      2nd year    CSE     Roll - 20

Print the month names of calendar.
"""

import calendar

for i in range(1,13):
    print("Month", str(i)+":", str(calendar.month_name[i]))
