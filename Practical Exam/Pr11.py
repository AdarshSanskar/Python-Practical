# Practical No. 11: Write a Program to Perform Create, add, delete, update, display operation on Dictionary
d = {'apple':10, 'banana':5, 'cherry':8}

#Adding an Item
d['date'] = 15
print(d)
#Update an Existing Item
d['banana'] = 12
print(d)
#Deleting an Item
del d['cherry']
print(d)
print("Updated Dictionary : ", d)