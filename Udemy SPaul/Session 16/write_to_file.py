

names = ['Tina', 'Rabi', 'Mathew', 'Rahman', 'Sandip', 'Liza', 'Peter', 'John']

with open('students.txt', 'w') as file_object:
    for name in names:
        file_object.write(name)
        file_object.write('\n')
