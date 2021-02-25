# Inheritance using Python.

class Human:
    def __init__(self, name):
        self.name = name

    def smile(self):
        print(self.name, ' is smiling - Ha ha ha')

    def walking(self):
        print(self.name, ' is walking')


class Student(Human):
    def __init__(self, roll_no, name):
        # super().__init__(name)
        Human.__init__(self, name)
        self.roll_no = roll_no

    def study(self):
        print('Student: ', self.name,'Roll: ', self.roll_no, 'is preparing for the exam')


class Teacher(Human):
    def __init__(self, dept_name, name):
        super().__init__(name)
        self.dept_name = dept_name

    def take_class(self):
        print('Teacher: ', self.name, 'taking class for department: ', self.dept_name)


s1 = Student(1, 'John')
t1 = Teacher( 'Computer Science', 'Malik')

s1.smile()
t1.smile()

s1.study()
t1.take_class()



