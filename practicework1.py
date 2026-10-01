
def list_student():
    student_list = []
    for i in range(1, 3):
        student_list.append(input(f"Enter student {i} information (id, name, dob): ").split(","))
    return student_list

def list_subject():
    subject_list = []
    for i in range(1, 3):
        subject_list.append(input(f"Enter subject {i} information (id, name): ").split(","))
    return subject_list

def list_marks():
    marks_list = []
    for i in range(1, 3):
        marks_list.append(input(f"Enter marks for student {i}: ").split(","))
    return marks_list

def display_student_marks(student_list, subject_list, marks_list):
    for student in student_list:
        student_id = student[0]
        student_name = student[0]
        for subject, marks in zip(subject_list, marks_list):
            subject_id = subject[0]
            subject_name = subject[0]
            student_marks = marks[0]
            print(f"Subject ID: {subject_id}, Name: {subject_name}, Marks: {student_marks}")

def student_GPA(list_marks):
    total_marks = 0
    for marks in list_marks:
        total_marks += sum(map(int, marks))
    gpa = total_marks / (len(list_marks) * len(list_marks[0]))
    return gpa


def save_to_file(student_list, subject_list, marks_list):
    with open("student.dat", "w") as f:
        for student in student_list:
            student_id = student[0]
            student_name = student[1]
            f.write(f"Student ID: {student_id}, Name: {student_name}\n")
            for subject, marks in zip(subject_list, marks_list):
                subject_id = subject[0]
                subject_name = subject[1]
                student_marks = marks[0]
                f.write(f"Subject ID: {subject_id}, Name: {subject_name}, Marks: {student_marks}\n")
            f.write("\n")


