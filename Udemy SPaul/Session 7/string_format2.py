# format method
names = ["John", "Raghuvir", "Jinia", "Tina", "Ali", "Razia", "Noble", "Tania"]
scores = [94.93271, 97.54123, 67.56786, 69.45543, 89.88765, 87.67125, 87.45676, 78.98124]

heading = "{0:20} {1:>10}".format("Names", "Scores")
print(heading)
print()

for name, score in zip(names, scores):
    str = "{0:.<20} {1:10.2f}".format(name, score)
    print(str)









