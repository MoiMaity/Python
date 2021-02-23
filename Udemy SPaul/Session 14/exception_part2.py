# exception handling in Python
students = {1:9.97, 2:7.89, 3:8.25, 4:8.95, 5:8.75}
print('Students:', students)

while True:
    try:
        target = int(input('Input id of student that you want to remove: '))
        if target == 0:
            break
        del_score = students.pop(target)
        if not students:
           break
        print('Student',target,'deleted, the student scored:',del_score)

    except KeyError as ke:
        print('Invalid key, key does not exists')

    except Exception as e:
        print('Some excepion handled', e.args)

    # except ValueError as ve:
    #     print('Invalid input found')
    # except KeyError as ke:
    #     print('The key you mentioned is not there')

print('Students:', students)



