# Assignment 4 - Parsing & Sorting Student Data in Python

## **Overview**
This project is a Python implementation of **Assignment #4** from Coders Campus, which involves parsing a "master list" of student enrollments and separating them into course-specific CSV files. The original assignment was written in Java, and I translated it into Python while ensuring it maintained the same behavior.

---

## **Original Java Assignment Instructions**

### **Objective**
A college has provided a **single CSV file** containing all student enrollments across multiple courses. The goal is to **filter** and **separate** the students into individual CSV files, each corresponding to a specific course.

### **Requirements**
1. **Parse the master list CSV file** and read student data into memory.
2. **Group students by their respective courses** (e.g., COMPSCI, APMTH, STAT).
3. **Sort each course’s students by grade in descending order.**
4. **Write the sorted students to separate CSV files**:
   - `course1.csv` (e.g., COMPSCI students)
   - `course2.csv` (e.g., APMTH students)
   - `course3.csv` (e.g., STAT students)

### **Hints**
- Be mindful of **null values** when sorting.
- When writing to a file, `"\n"` can be used to create new lines.
- Convert **string numbers** into **integers** before sorting:
  ```java
  Integer myIntVal = Integer.parseInt(myStringVal);
  ```

### **Example Output Files**
#### **course1.csv** (COMPSCI Students)
```csv
Student ID,Student Name,Course,Grade
28,Justin Conrad,COMPSCI 310,99
37,Simone Scott,COMPSCI 312,91
91,Donald Schultz,COMPSCI 321,87
...
```
#### **course2.csv** (APMTH Students)
```csv
Student ID,Student Name,Course,Grade
89,Alison Murray,APMTH 134,93
59,Amber-Rose Austin,APMTH 129,93
68,Aran Rice,APMTH 131,89
...
```
#### **course3.csv** (STAT Students)
```csv
Student ID,Student Name,Course,Grade
15,Padraig Barry,STAT 236,93
39,Zachariah Hutchinson,STAT 240,92
33,Stewart Reed,STAT 239,90
...
```

---

## **Translating This to Python**
### **Challenges & Lessons Learned**

### **1️⃣ Java’s `BufferedReader` vs. Python’s `csv.reader`**
- Java requires `BufferedReader` to read files line by line.
- Python’s `csv.reader` provides a **cleaner approach**:
  ```python
  with open('student-master-list.csv', mode='r') as csv_file:
      reader = csv.DictReader(csv_file)
      for row in reader:
          students.append(Student(row["Student ID"], row["Student Name"], row["Course"], row["Grade"]))
  ```

### **2️⃣ Handling Case-Sensitive Course Names**
- In Java, we might check for prefixes manually.
- In Python, `startswith()` works well:
  ```python
  if student.course_id.startswith("COMPSCI"):
      compsci_students.append(student)
  ```

### **3️⃣ Sorting Data in Descending Order**
- Java’s `Arrays.sort()` requires a **custom comparator**.
- Python’s `sorted()` is simpler:
  ```python
  sorted_students = sorted(students, key=lambda student: student.grade, reverse=True)
  ```

---

## **Python Implementation**

### **`student.py`** (Student Data Model)
```python
class Student:
    def __init__(self, id, name, course_id, grade):
        self.id = id
        self.name = name
        self.course_id = course_id
        self.grade = int(grade)  # Ensure grades are integers

    def __repr__(self):
        return f'Student({self.id}, {self.name}, {self.course_id}, {self.grade})'
```

### **`csv_utils.py`** (Reading & Writing CSV Files)
```python
import csv
from student import Student

MASTER_CSV_PATH = "resource/student-master-list.csv"
COURSE_CSV_TEMPLATE = "resource/course{}.csv"

def load_students_from_csv():
    students = []
    try:
        with open(MASTER_CSV_PATH, mode='r', encoding="utf-8-sig") as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                students.append(Student(row["Student ID"], row["Student Name"], row["Course"], row["Grade"]))
    except FileNotFoundError:
        print(f"File '{MASTER_CSV_PATH}' not found.")
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
```

### **`student_parser.py`** (Sorting & Processing Data)
```python
import csv_utils

def sort_students_by_course_and_grade(students, course):
    return sorted(
        [student for student in students if student.course_id.startswith(course)],
        key=lambda student: student.grade,
        reverse=True
    )

def parse_students(courses):
    students = csv_utils.load_students_from_csv()
    for index, course in enumerate(courses):
        sorted_students = sort_students_by_course_and_grade(students, course)
        csv_utils.write_students_to_csv(sorted_students, csv_utils.COURSE_CSV_TEMPLATE.format(index + 1))
```

### **`main.py`** (Entry Point)
```python
from student_parser import parse_students

if __name__ == "__main__":
    courses = ["COMPSCI", "APMTH", "STAT"]
    parse_students(courses)
```

---

## **Conclusion**
✅ Successfully implemented **student data parsing and sorting in Python**.  
✅ Learned key differences between **Java and Python file handling, sorting, and list filtering**.  
✅ **Python’s `csv` module made file I/O simpler** than Java’s `BufferedReader`.  

**Next steps:** Add a **command-line interface (CLI)** for better usability! 🚀🐍

---

**🛠️ Built With:**
- Python 3
- No external libraries (pure Python implementation)

📌 **Author:** [Your Name]  
📌 **GitHub Repo:** [Your Repo Link]

🚀 **Excited for the next challenge!**

