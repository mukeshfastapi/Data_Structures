# Python File to delete values in 2D Array

# creating 2D Array using numpy
import numpy as np

# creating 2D Array
arr = np.array([[1, 10, 19], [20, 25, 29], [30, 35, 39]])

print(arr)
# delete row 1 (2nd row)
# result = np.delete(arr, 1, axis=0)
# print(result)

# delete column 1(2nd column)
# result = np.delete(arr, 1, axis=1)
# print("After deleted column")
# print(result)

# Delete a specific element (Not common --->Risky operation)
result = np.delete(arr, arr[0, 0])
print(result)