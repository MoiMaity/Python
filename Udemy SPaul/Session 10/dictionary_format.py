student = {'name':'Rambo', 'gpa':9.1, 'grade':'O'}

#fmt_string = 'Name of student: {0[name]}, GPA: {0[gpa]} and Grade: {0[grade]}'.format(student)
fmt_string = f'Name of student: {student["name"]}, GPA: {student["gpa"]} and Grade: {student["grade"]}'
print(fmt_string)