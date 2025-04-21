# Practical No. 12: Write a program to create, union, intersect, difference, symmetric difference operation on set
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

union_set = a | b
intersect_set = a & b
diff_set = a - b
sym_diff_set = a ^ b

print("Set A:", a)
print("Set B:", b)
print("Union:", union_set)
print("Intersection:", intersect_set)
print("Difference (A - B):", diff_set)
print("Symmetric Difference:", sym_diff_set)
