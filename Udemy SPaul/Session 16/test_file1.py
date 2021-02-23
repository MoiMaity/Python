# file handling in Python
#file_object = open('names.txt', 'r')  # 1. read - 'r', 2. write - 'w', 3. append - 'a'

with open('names.txt', 'r') as file_object:
    print('Is the file closed? ', file_object.closed)
    print(file_object.readline())

print('Is the file closed? ', file_object.closed)
# lines = file_object.readlines()
# print(lines, type(lines))
# file_object.close()
