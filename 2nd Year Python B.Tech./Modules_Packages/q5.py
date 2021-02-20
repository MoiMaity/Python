"""
programs to print first monday and name of months in a given year
@author:  Aradhita Dasgupta      2nd year    CSE     Roll - 20
"""


import calendar

n = int(input("Enter a year: "))

c=calendar.Calendar(calendar.MONDAY)

for i in range(12):
    d=c.monthdayscalendar(n,i+1)
    print(calendar.month_name[i+1]," = "+str(d[0][0] if d[0][0]!=0 else d[1][0]))
