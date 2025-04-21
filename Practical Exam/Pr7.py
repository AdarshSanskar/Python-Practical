# Practical No. 7: Write a Program to Check if a number is Positive, Negative or Zero
def checkNumber(num):
    if num > 0:
        print("The Number is Positive...")
    elif num < 0:
        print("The Number is Negative...")
    else:
        print("The Number is Zero...")

num = int(input("Enter any Number : "))
checkNumber(num)