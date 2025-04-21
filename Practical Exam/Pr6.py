#Practical No. 6: Write a Program to create user defined Function to Check Leap Year
def checkLeapYear(year):
    if year % 4 == 0:
        print("The Year is Leap Year...")
    else:
        print("The Year is Not Leap Year...")

y = int(input("Enter any Year : "))
checkLeapYear(y)