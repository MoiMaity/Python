students = ['John', 'Lucy', 'Peter', 'Abir', 'Mike']
grades = ['A', 'A', 'O', 'B', 'C']
points = [8.5, 8.75, 9.5, 7.5, 6.25]

for student, grade, point in zip(students, grades, points):
    print(f'Student {student} achieved grade {grade} with point {point}')