#Practical No. 3: Write a Program to check Largest Number among the three numbers
a = int(input("Enter Number 1: "))
b = int(input("Enter Number 2: "))
c = int(input("Enter Number 3: "))
if a>b and a>c:
    print("A is Greatest")
elif b>a and b>c:
    print("B is Greatest")
else:
    print("C is Greatest")