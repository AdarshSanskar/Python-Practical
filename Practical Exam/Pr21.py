# Practical No. 21: Write a Program to implement concept of parameterized constructor
class Student:
    def __init__(self, name, roll):
        self.name = name
        self.roll = roll

    def display(self):
        print("Name:", self.name)
        print("Roll Number:", self.roll)

s1 = Student("Ravi", "23")
s2 = Student("Pooja", "45")

s1.display()
s2.display()
