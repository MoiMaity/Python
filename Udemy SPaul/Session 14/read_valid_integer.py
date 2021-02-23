def read_valid_integer(prompt):
    val = 0
    is_valid = False

    while not is_valid:
        is_valid = True
        try:
            val = int(input(prompt))
        except Exception as e:
            print('You gave an invalid formatted integer')
            is_valid = False

    return val


def main():
    age = read_valid_integer('Input your age: ')
    print('Your age is', age)

    id = read_valid_integer('Enter your id: ')
    print('Your id is: ', id)

if __name__ == '__main__':
    main()