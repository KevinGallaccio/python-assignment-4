import csv_utils


def sort_students_by_course_and_grade(students, course):
    sorted_students = sorted(
        [student for student in students if student.course_id.startswith(course)],
        key=lambda student: student.grade,
        reverse=True)
    return sorted_students


def parse_students(courses):
    students = csv_utils.load_students_from_csv("resource/student-master-list.csv")
    for index, course in enumerate(courses):
        sorted_students = sort_students_by_course_and_grade(students, course)
        csv_utils.write_students_to_csv(sorted_students, f"resource/course{index + 1}.csv")
