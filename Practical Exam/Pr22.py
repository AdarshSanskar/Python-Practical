# Practical No. 22: Write a Program to implement concept of lambda function
add = lambda a, b: a + b
sub = lambda a, b: a - b
mul = lambda a, b: a * b
div = lambda a, b: a / b

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Addition:", add(a, b))
print("Subtraction:", sub(a, b))
print("Multiplication:", mul(a, b))
print("Division:", div(a, b))
