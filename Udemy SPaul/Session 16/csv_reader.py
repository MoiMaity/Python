import csv

with open('employee.csv', 'r') as file_object:
    csv_reader = csv.reader(file_object)
    line_no = 0
    for rec in csv_reader:
        print (rec)
        if line_no == 0:
            print(f'Rec No  {rec[0]:10} {rec[1]:20} {rec[2]:10} {rec[3]:20}')
            print('-' * 70)
        else:
            print(f'{line_no:>8} {rec[0]:10} {rec[1]:20} {rec[2]:>10} {rec[3]:20}')
        line_no += 1


