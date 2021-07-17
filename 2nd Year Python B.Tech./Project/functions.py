import openpyxl

class Student_info:
    def __init__(self):
        self.info = {}
        
    def input(self, name, dept, year, roll):
        self.info["name"] = name
        self.info["dept."] = dept
        self.info["year"] = year
        self.info["roll"] = roll
        
    def __str__(self):
        return self.info["name"] + "\tDept. - " + self.info["dept."] + "\tyear - " + str(self.info["year"]) + "\troll no. - " + str(self.info["roll"])

    

def openxl(filename, heading):

    try:
        db = openpyxl.load_workbook(filename)
        ds = db["Students"]
        first_row = list(ds.rows)[0]
        for i in range (len(first_row)):
            if heading[i] != first_row[i].value:
                "s"+4
        return db, ds
    except:
        db = openpyxl.Workbook()
        db.active.title = "Students"
        ds = db.active
        ds.append(heading)
        db.save(filename)
        return db, ds
    

def take_input():
    student = Student_info()
    name = input("Enter student's name: ")
    dept = input("Enter student's current department: ")
    year = input("Enter student's current year: ")
    roll = int(input("Enter student's current roll number: "))
    
    student.input(name, dept, year, roll)
    return student

    
def entry(ds, student):
    ds.append(list(student.info.values()))
    
    return student.__str__()
