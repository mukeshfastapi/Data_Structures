# Creating a 2D array using Numpy

import numpy as np

arr = np.array([[1, 2, 3], [10, 20, 30], [100, 200, 300]])

print(arr)

# Inserting values in coloumn in an 2D Array
new_arr = np.insert(arr, 1, [25, 23, 26], axis=1)
print("New Array...")
print(new_arr)

# Inserting values in coloumn in an 2D Array
new_arr1 = np.insert(arr, 0, values=[33, 35, 36], axis=0)
print("Inserting a row in my 2D Array")
print(new_arr1)

# Appending a new row (must be 2D and same length as existing columns)
new_arr2 = np.append(arr, [[89, 99, 100]], axis=0)
print("\nNew Array After Row Append:")
print(new_arr2)