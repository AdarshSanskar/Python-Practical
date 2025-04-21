# Practical No. 15: Write Python program to display 2D bar graph using package.
import matplotlib.pyplot as plt

x = ['A','B','C','D']
y = [10,15,7,12]

plt.bar(x,y)
plt.xlabel("Categories")
plt.ylabel("Values")
plt.title("2D Bar Graph")
plt.show()