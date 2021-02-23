with open('input.txt', 'rb') as file_object:
    file_object.seek(10)
    pos = file_object.tell()
    print('Position =', pos)
    file_object.seek(-5, 1)
    pos = file_object.tell()
    print('Position =', pos)
    file_object.seek(0, 2)
    pos = file_object.tell()
    print('Position =', pos)
    file_object.seek(-4, 2)
    content = file_object.read(4)
    print(content.decode('ascii'))


