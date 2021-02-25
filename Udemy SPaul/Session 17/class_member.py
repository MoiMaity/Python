
class Student:

    pass_score = 40.0

    def __init__(self, roll, first_name, last_name, score):
        self.roll = roll
        self.first_name = first_name
        self.last_name = last_name
        self.score = score
        self.email = first_name.lower() + "." + last_name.lower() + "@schooldomain.com"

    def name(self):
        return self.first_name + " " + self.last_name

    def pass_or_fail(self):
        if self.score >= Student.pass_score:
            return "Passed"
        else:
            return "Failed"


print('Pass score is: ', Student.pass_score)
print('Content of class student:', Student.__dict__)
s1 = Student(1, 'Shibaji', 'Paul', 75.0)
s2 = Student(2, 'John', 'Rambo', 35.5)

# print('Content of s1:', s1.__dict__)
print(s1.pass_or_fail())
print(s2.pass_or_fail())
# print('Using s1: ', s1.pass_score)


# # Student.name(s1)
# print(s1.roll, s1.name(), s1.email, type(s1))
# print(s2.roll, Student.name(s2), s2.email, type(s2))


