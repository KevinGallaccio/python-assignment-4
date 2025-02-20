import csv_utils


def sort_students_by_course_and_grade(students, course):
    sorted_students = sorted(
        [s for s in students if s.course_id.startswith(course)],
        key=lambda student: student.grade,
        reverse=True)
    return sorted_students


def parse_students(courses):
    students = csv_utils.load_students_from_csv()
    for index, course in enumerate(courses):
        sorted_students = sort_students_by_course_and_grade(students, course)
        csv_utils.write_students_to_csv(sorted_students, csv_utils.COURSE_CSV_TEMPLATE.format(index + 1))
