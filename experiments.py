class Student:
    def __init__(self,name,age,grade):
        self.name=name
        self.age=age
        self.grade=grade
    def get_grade(self):
        return self.grade
class Course:
    def __init__(self,name,max_students):
        self.name = name
        self.max_students = max_students
        self.students= []
    def addstudent(self,student):
        if len(self.students)<self.max_students:
            self.students.append(student)
    def dispAll(self):
        print(self.students)
    def getavg(self):
        pass
s1 = Student("student1",20,30)
s2 = Student("Hello",30,50)
c1 = Course("CS",2)
c1.addstudent(s1)
c1.dispAll()

print(Student.get_grade(s1))