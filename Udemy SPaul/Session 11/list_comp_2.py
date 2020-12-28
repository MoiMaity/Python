
# list comprehension

# a_list = [101, 55, 40, 24, 78, 200, 75, 19, 16, 43]
# b_list = [p * 3 for p in a_list if p % 2 != 0]
# print(b_list)

students = {'John':8.9, 'Peter':9.1, 'Kate':6.7, 'Tania':9.8, 'Tina':8.7}
grade_o = {name:'O' for name, gpa in students.items() if gpa >= 9.0}
print(grade_o)













