# Practical No. 23: Write a Python Function that accept a string and calculate the number of upper case letters and lower case letter
def count_case(s):
    upper = 0
    lower = 0
    for ch in s:
        if ch.isupper():
            upper += 1
        elif ch.islower():
            lower += 1
    print("Uppercase letters:", upper)
    print("Lowercase letters:", lower)

text = input("Enter a string: ")
count_case(text)
