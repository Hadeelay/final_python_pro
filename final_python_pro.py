
"""ITF 07 Final Project Attendance System
# TODO 1 Enter your name and submission date
Name :Hadeel Daher
Delivery Date :25/6/2023
"""

class Course:
    def __init__(self, name, mark):
        self.course_id = uuid.uuid4()
        self.name = name
        self.mark = mark

class Student:
    total_student = 0
    def __init__(self, name):
        self.name = name
        Student.total_student += 1

    def __init__(self, name, age, number):
        self.student_id = uuid.uuid4()
        self.name = name
        self.age = age
        self.number = number
        self.courses = []

    def enroll_course(self, course):
            self.courses.append(course)

    def get_student_info(self):
            return self.__dict__

    def get_student_courses(self):
            for course in self.courses:
                print(f"{course.name}: {course.mark}")

    def get_student_average(self):
            total_marks = 0
            for course in self.courses:
                total_marks += course.mark
            return total_marks / len(self.courses)

while True:
    try:
        selection = int(input("1.Add New Student\n"
                              "2.Delete Student\n"
                              "3.Display Student\n"
                              "4.Get Student Average\n"
                              "5.Add Course to student with mark.\n"
                              "6.Exit"))
    except ValueError:
        print("Invalid input, please enter a number between 1 and 6.")
        continue

    if selection == 1:
        student_number = input("Enter Student Number")
        Is_existing_student = False
        for student in students:
            if student.number == student_number:
                is_existing_student = True
                break

        if is_existing_student:
            print("Student with this number exists.")
        else:
            student_name = input("Enter Student Name")
            while True:
                try:
                    student_age = int(input("Enter Student Age"))
                    break
                except:
                    print("Invalid Value")

            student_courses = []
            students.append(student)

            print("Student Added Successfully")

    elif selection == 2:
        student_number = input("Enter Student Number")
        target_student = None
        for student in mystudents:
            if student.number == student_number:
                target_student = student
                break

        if target_student:
            students.remove(target_student)
            print("Student Deleted Successfully")
        else:
            print("Student Not Exist")

    elif selection == 3:
        student_number = input("Enter Student Number")
        target_student = None
        for student in mystudents:
            if student.number == student_number:
                target_student = student
                break

        if target_student:
            student_info = target_student.get_student_info()
            print(f"Student Name: {student_info['name']}")
            print(f"Student Age: {student_info['age']}")
            print(f"Student Number: {student_info['number']}")
            target_student.get_student_courses()
        else:
            print("Student Not Exist")

    elif selection == 4:
        student_number = input("Enter Student Number")
        target_student = None
        for student in students:
            if student.number == student_number:
                target_student = student
                break

        if target_student:
            print(f"Student Average: {target_student.get_student_average()}")
        else:
            print("Student Not Exist")

    elif selection == 5:
        student_number = input("Enter Student Number")
        target_student = None
        for student in mystudents:
            if student.number == student_number:
                target_student = student
                break

        if target_student:
            course_name = input("Enter Course Name")
            while True:
                try:
                    course_mark = int(input("Enter Course Mark"))
                    break
                except:
                    print("Invalid Value")
            course = Course(course_name, course_mark)
            target_student.enroll_course(course)
            print("Course Added Successfully")
        else:
            print("Student Not Exist")

    else:
        exit_program()