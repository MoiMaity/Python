name1 = "Anand"
name2 = "John"
duration = 10
score1 = 10.786
score2 = 19.456

#str = "{0} and {1} are friends for {2} years".format(name1, name2, duration)
str = f"{name1:.<20} and {name2:20} are friends for {duration:15.2f} years"
print(str)


