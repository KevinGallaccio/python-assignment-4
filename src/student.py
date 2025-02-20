class Student:

    def __init__(self, id, name, course_id, grade):
        self.id = id
        self.name = name
        self.course_id = course_id
        self.grade = grade

    def __repr__(self):
        return f'User({self.id}, {self.name}, {self.course_id}, {self.grade})'
