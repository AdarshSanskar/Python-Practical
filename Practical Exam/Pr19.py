# Practical No. 19: Implement a Program for Multilevel Inheritance
class Student:
    def accept(self):
        self.name = input("Enter Name: ")
        self.roll = input("Enter Roll Number: ")

class Marks(Student):
    def get_marks(self):
        self.m1 = int(input("Enter Marks 1: "))
        self.m2 = int(input("Enter Marks 2: "))

class Result(Marks):
    def display(self):
        print("Name:", self.name)
        print("Roll Number:", self.roll)
        print("Marks 1:", self.m1)
        print("Marks 2:", self.m2)
        total = self.m1 + self.m2
        print("Total:", total)
        print("Percentage:", total / 2)

r = Result()
r.accept()
r.get_marks()
r.display()
