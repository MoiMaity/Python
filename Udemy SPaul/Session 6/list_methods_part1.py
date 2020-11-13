students = ["Teddy", "Saloni", "Nikita", "John", "Frank", "Ali", 10, 20, 5.6, [3.5, 6.7, 7.9]]
# for i in students:
#     print(i)
#
# x = students[-1][1]
# print(x)
# students[-1][1] = 9.99
# print(students)

# print(students)
# #students.extend("Tina")
# lst1 = ["Tina", "Raj", "Bob"]
# students.extend(lst1)
# print(students)


print(students)
students.insert(0, "Bob")
print(students)

students.insert(2, "Tina")
print(students)
stud = students.copy()
print('Content of stud', stud)