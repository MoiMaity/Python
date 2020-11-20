
name1 = "Anand"
name2 = "John"
duration = 10
score1 = 10.786
score2 = 19.456

str = name1 + " and " + name2 + " are friends for " + str(duration) + " years!"


str = "{0:^20} and {1} are friends for {2:^10} years".format(name1, name2, duration)
print(str)

names = ["John", "Raghuvir", "Jinia", "Tina", "Ali", "Razia", "Noble", "Tania"]
marks = [100, 97, 67, 9, 100, 87, 4, 55]

print("{0:20}  {1:6}".format("Name", "Marks"))

for name, mark in zip(names, marks):
    print("{0:20} {1:6}".format(name, mark))
