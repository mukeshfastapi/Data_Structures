# Python code for traversing the 2D Array

# creating 2D Array using numpy
import numpy as np

# creating 2D Array
arr = np.array([[1, 10, 19], [20, 25, 29], [30, 35, 39]])

print(arr)
print("Row")
for row in arr:
    print(row)

print("Row and Column")

# for i in range(arr.shape[0]):
#     for j in range(arr.shape[1]):
#         print(arr[i][j], end=" ")
#     print()

for i in range(len(arr)):
    for j in range(len(arr[i])):
        print(arr[i][j], end=" ")
    print()