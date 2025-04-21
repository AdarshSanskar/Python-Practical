#Practical No. 14: Write a Program to create two matrices and perform addition and subtraction on matrix using numpy package
import numpy as np
a = np.array([[1,2],[3,4]])
b = np.array([[5,6],[7,8]])

add = a + b
sub = a - b

print("Matrix A : \n",a)
print("Matrix B : \n",b)
print("Addition : \n",add)
print("Subtraction : \n",sub)