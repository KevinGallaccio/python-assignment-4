import csv
from student import Student


def load_students_from_csv(file_path):
    students = []
    try:
        with open(file_path, mode='r', encoding="utf-8-sig") as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                student = Student(row["Student ID"], row["Student Name"], row["Course"], row["Grade"])
                students.append(student)
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
    return students


def write_students_to_csv(students, file_name):
    try:
        with open(file_name, mode='w', newline='', encoding="utf-8") as csv_file:
            fieldnames = ['Student ID', 'Student Name', 'Course', 'Grade']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()
            for student in students:
                writer.writerow({
                    'Student ID': student.id,
                    'Student Name': student.name,
                    'Course': student.course_id,
                    'Grade': student.grade
                })
    except Exception as e:
        print(f"An error occurred while writing to the file: {e}")
