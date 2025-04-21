#Practical No. 2: Write a Program to swap two Variables
num1 = int(input("Enter Number 1: "))
num2 = int(input("Enter Number 2: "))
print("Value Before Swapping: ")
print("A : ",num1,"B : ",num2)
temp = num1
num1 = num2
num2 = temp
print("Value After Swapping: ")
print("A : ",num1,"B : ",num2)