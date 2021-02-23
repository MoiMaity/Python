with open('test_file.txt', 'w+') as file_object:
    file_object.write("Hello, this is the first content")
    file_object.seek(0)
    content = file_object.read(5)
    print(content)

