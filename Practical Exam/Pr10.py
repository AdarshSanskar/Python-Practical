# Practical No. 10: Write a Program to Perform Create, add, delete, update, display operation on list
list = [10,20,30,40,50]

list.append(60)
print(list)
list.insert(2,25)
print(list)
list.remove(40)
print(list)
list.pop()
print(list)
list[0] = 5
print(list)
lengthList = len(list)
print("Length of String : ", lengthList)
sumList = sum(list)
print("Sum of List : ", sumList)
list.sort()
print(list)
list.sort(reverse=True)
print(list)
list.reverse()
print(list)
