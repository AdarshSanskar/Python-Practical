#Practical No. 4: Write a Program that takes the marks of 5 Subjects and display grade ladder using if else
m1 = int(input("Enter Marks of Subject 1: "))
m2 = int(input("Enter Marks of Subject 2: "))
m3 = int(input("Enter Marks of Subject 3: "))
m4 = int(input("Enter Marks of Subject 4: "))
m5 = int(input("Enter Marks of Subject 5: "))
total = m1+m2+m3+m4+m5;
avg = total/5;
if avg >= 90 and avg <= 100:
    print("Grade A")
elif avg >= 80 and avg < 90:
    print("Grade B")
elif avg >= 70 and avg < 80:
    print("Grade C")
elif avg >= 60 and avg < 70:
    print("Grade D")
else:
    print("Fail")