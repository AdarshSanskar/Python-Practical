# Practical No.16 : Write a program to perform arithmetic operation using user defined module.
import Pr16_Module as maths

a = int(input("Enter First Number : "))
b = int(input("Enter Second Number : "))

print("Addition : ", maths.add(a, b));
print("Subtraction : ", maths.sub(a, b));
print("Multiplication : ", maths.mult(a, b));
print("Division : ", maths.div(a, b));
