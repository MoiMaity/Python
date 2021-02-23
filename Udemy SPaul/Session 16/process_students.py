
def get_grade(average):
    if average >= 90.0:
        return 'A'
    elif average >= 80.0:
        return 'B'
    elif average >= 70.0:
        return 'C'
    elif average >= 60.0:
        return 'D'
    else:
        return 'F'


def print_report(students):
    with open('reports.txt', 'w') as file_object:
        for key, value in students.items():
            average = round(sum(value) / len(value), 2)
            grade = get_grade(average)
            print(key, average, grade, sep=' ', end='\n')
            file_object.write(key + ' ' + str(average) + ' ' + grade + '\n')


def read_file():
    students = dict()
    with open("students_data.csv", "r") as file_object:
        for rec in file_object:
            rec = rec[0:-1]
            data_parts = rec.split(",")
            students[data_parts[0]] = [int(n) for n in data_parts[1:]]
            #print(data_parts)

    return students


def main():
    students = read_file()
    # print(students)
    print_report(students)


if __name__ == '__main__':
    main()