import csv

with open('employee.csv', 'r') as file_object:
    csv_dict_reader = csv.DictReader(file_object)
    # print(csv_dict_reader.fieldnames)
    fieldnames = csv_dict_reader.fieldnames
    rec_no = 1
    print(f'Rec No   {fieldnames[0]:10} {fieldnames[1]:20} {fieldnames[2]:10} {fieldnames[3]:20}')
    print('-' * 80)
    for rec in csv_dict_reader:
        print(rec)
        print(f'{rec_no:>8} {rec[fieldnames[0]]:10} {rec[fieldnames[1]]:20} {rec[fieldnames[2]]:>10} '
              f'{rec[fieldnames[3]]:20}')
        rec_no += 1











