#Practical No. 5: Write a Program to create user defined Function to Check if a number is odd or even

def check(num):
    if num % 2 == 0:
        print("The Number is Even")
    else:
        print("The Number is Odd")

no = int(input("Enter any Number : "))
check(no)