import functions

filename = "student_info_trial.xlsx"

heading = ["Name", "Dept.", "Year", "roll no."]

db, ds = functions.openxl(filename, heading)

key = 1

while key:
    
    student = functions.take_input()
    print(functions.entry(ds, student) + "\nadded to the database.")
    
    key = int(input("Enter 1 to add more student's info.\nEnter 0 to exit."))
    
db.save(filename)
