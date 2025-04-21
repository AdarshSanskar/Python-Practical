#Practical No. 20: Implement a Python Program of Multiple Inheritance
class Personal:
    def get_personal(self):
        self.name = input("Enter Name: ")
        self.age = input("Enter Age: ")

class Academic:
    def get_academic(self):
        self.course = input("Enter Course: ")
        self.marks = int(input("Enter Marks: "))

class Student(Personal, Academic):
    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Course:", self.course)
        print("Marks:", self.marks)

s = Student()
s.get_personal()
s.get_academic()
s.display()
