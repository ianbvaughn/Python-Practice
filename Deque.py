from collections import deque

class Student:
    def __init__(self,grd):
        self.grade=grd
class Class:
    def __init__(self,name:str):
        self.name=name
        self.students = deque()
        self.student_grades = deque()
    def add_student(self,stud:Student):
        self.students.append(stud)
        self.student_grades.append(stud.grade)
    def get_grades(self) -> list:
        return [x for x in self.student_grades]
    def rotate_grades(self) -> None:
        self.student_grades.rotate(1)

geometry_class = Class("Geometry")

s = Student('A')
k = Student('B')
r = Student('C')

geometry_class.add_student(s)
geometry_class.add_student(k)
geometry_class.add_student(r)

print("Geometry Class Grades: ", geometry_class.get_grades())
geometry_class.rotate_grades()
print("Geometry Class Grades: ", geometry_class.get_grades())