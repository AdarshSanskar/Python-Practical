# Practical No. 17: Implement a class student with data members; Name, Roll number, Marks, Create Suitable method for reading, printing students details & calculate percentage
class Student:
    def getData(self):
        self.name = input("Enter Name : ")
        self.roll = int(input("Enter Roll Number : "))
        self.marks = []
        for i in range(5):
            m = int(input(f"Enter Marks for Subject {i+1} : "))
            self.marks.append(m)

    def displayData(self):
        print("Name : ",self.name)
        print("Roll Number : ",self.roll)
        print("Marks : ", self.marks)
        total = sum(self.marks)
        percentage = total / 5
        print("Percentage : ",percentage)

s = Student()
s.getData()
s.displayData()