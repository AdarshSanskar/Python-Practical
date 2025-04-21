# Practical No. 18: Implement a program of Simple inheritance create class student having members roll and name accept and display details for 2 Students
class Student:
    def acceptData(self):
        self.name = input("Enter Name : ")
        self.roll = input("Enter Roll Number : ")

class Info(Student):
    def displayData(self):
        print("Name : ", self.name)
        print("Roll Number : ", self.roll)

s1 = Info()
s2 = Info()

print("Enter Detail of Both Students : ")
s1.acceptData()
s2.acceptData()

print("Deails of Students: ")
s1.displayData()
s2.displayData()


