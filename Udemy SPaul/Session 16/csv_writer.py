import csv

employees = [
                ['E001', 'John Rambo', '7000.0', 'Sales'],
                ['E002', 'Tina Munim', '6575.0', 'Production'],
                ['E003', 'James Smith', '9875.0', 'Design']
            ]
with open('emp1.csv', 'w', newline='') as file_object:
    csv_writer=csv.writer(file_object, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    for e in employees:
        csv_writer.writerow(e)
