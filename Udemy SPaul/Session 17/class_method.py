
class Student:

    pass_score = 40.0
    # from_string_counter = 0

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

    @classmethod
    def update_score(cls, new_score):
        cls.pass_score = new_score

    @staticmethod
    def from_string(str_student):
        str_roll, str_first_name, str_last_name, str_score = str_student.split(",")
        s = Student(int(str_roll), str_first_name, str_last_name, float(str_score))
        # cls.from_string_counter += 1
        return s



str1 = "1,James,Smith,67.5"
str2 = "2,David,Smith,76.75"
str3 = "3,James,Johnson,90.5"

s1 = Student.from_string(str1)
s2 = Student.from_string(str2)
s3 = Student.from_string(str3)

s4 = Student(4, 'FNAme', 'LName', 90.0)

print(s1.email, s2.email, s3.email, sep='\n')
# print(Student.from_string_counter)


#
# s1 = Student(1, 'Shibaji', 'Paul', 75.0)
# s2 = Student(2, 'John', 'Rambo', 35.5)
# print(Student.pass_score)
# Student.update_score(70.0)
# print(Student.pass_score)
#
