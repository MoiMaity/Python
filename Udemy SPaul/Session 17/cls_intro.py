
class Student:

    pass_score = 30.0

    def __init__(self, roll, first_name, last_name):
        self.roll = roll
        self.first_name = first_name
        self.last_name = last_name
        self.email = first_name.lower() + "." + last_name.lower() + "@schooldomain.com"

    def name(self):
        return self.first_name + " " + self.last_name


s1 = Student(1, 'Shibaji', 'Paul')
s2 = Student(2, 'John', 'Rambo')

# Student.name(s1)
print(s1.roll, Student.name(s1), s1.email, type(s1))
print(s2.roll, Student.name(s2), s2.email, type(s2))


