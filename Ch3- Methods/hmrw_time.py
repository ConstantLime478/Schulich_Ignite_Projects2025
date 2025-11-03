import os
import sys
import student_class
from student_class import Student

Student1 = Student("Hayyan")

Student1.add_homework(85)
Student1.get_num_questions()

print(Student1.name + " has " + Student1.get_num_questions() + " questions to do.")