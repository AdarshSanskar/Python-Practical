#Practical No. 13: Write a Python Program to print the numbers in word for example 1234 -> One Two Three Four
num = input("Enter a Number : ")
words = {'0':'Zero', '1':'One', '2':'Two', '3':'Three', '4':'Four', '5':'Five', '6':'Six', '7':'Seven', '8':'Eight', '9':'Nine'}

for digit in num:
    print(words[digit],end=' ')
