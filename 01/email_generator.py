import csv
import sys

def read_csv_file(file_path):
    names = []
    tasks = []
    grades = []

    try:
        with open(file_path, newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                names.append(row['name'] + " " + row['surname'])
                tasks.append(int(row['missings']))
                try:
                    grades.append(int(row['grade']))
                except ValueError:
                    grades.append(0)
    except FileNotFoundError:
        print('Nie ma takiego pliku!')
        sys.exit()

    return names, tasks, grades

def read_message(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        message = file.read()
    return message

def main():
    file_path = 'students.csv'
    names, tasks, grades = read_csv_file(file_path)

    message_path = 'message.txt'
    message = read_message(message_path)
    message_path_2 = 'message_2.txt'
    message2 = read_message(message_path_2)

    for i in range(len(names)):
        missing_tasks = tasks[i]
        current_grade = grades[i]
        potential_grade = current_grade + 1

        if current_grade == 6:
            formatted_message = message2.format(names[i], missing_tasks, current_grade,)
        else:
            formatted_message = message.format(names[i], missing_tasks, current_grade, potential_grade)

        print(formatted_message)
        print('_________________________________________________________________________')

if __name__ == '__main__':
    main()