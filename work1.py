from practicework1 import *

print("Displaying student marks:", display_student_marks(
list_student(), list_subject(), list_marks()
))

print("Student1 GPA:", student_GPA(list_marks()))   
print("Student2 GPA:", student_GPA(list_marks()))


            
print("Data saved to student.dat", save_to_file(list_student(), list_subject(), list_marks()))