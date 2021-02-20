# writing user defined functions in Python

def say_hello(name, age):
    print('--- In the function ----')
    if age <= 20:
        print('Hello!', name)
    else:
        print('Hey!! ', name)
    print('Hope you are liking this course')
    print()

# random.uniform(10.0, 20.0)
print('The program started')
say_hello('John', 25) # calling the function
print('Back to main flow')
say_hello('Peter', 14)
print('Bye!!')

