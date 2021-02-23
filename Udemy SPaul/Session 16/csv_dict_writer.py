import csv
employees = [
    {'emp_no': 'E001', 'name': 'John Rambo', 'basic': '7000.0', 'dept': 'Sales'},
    {'emp_no': 'E002', 'name': 'Tina Munim', 'basic': '6575.0', 'dept': 'Production'},
    {'emp_no': 'E003', 'name': 'James Smith', 'basic': '9875.0', 'dept': 'Design'}
]

with open('emp2.csv', 'w', newline='') as file_object:
    fieldnames = ['emp_no', 'name', 'basic', 'dept']
    csv_dict_writer = csv.DictWriter(file_object, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL,
                                     fieldnames=fieldnames)
    csv_dict_writer.writeheader()
    # csv_dict_writer.writerows(employees)
    for e in employees:
        csv_dict_writer.writerow(e)