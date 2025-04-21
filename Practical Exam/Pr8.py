#Practical No. 8: Write a Program to Find the number of digits in a number
def findDigit(num):
    cnt = 0
    while num > 0:
        rem = num % 10
        cnt = cnt + 1
        num = num // 10
    print("Number of Digits in Number : ", cnt)

no = int(input("Enter Any Number : "))
findDigit(no)

