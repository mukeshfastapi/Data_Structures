# creating 2D Array using numpy
import numpy as np

# creating 2D Array
arr = np.array([[1, 10, 19], [20, 25, 29], [30, 35, 39]])

print(arr)

# Accessing specific value from an Array(10)(39)
print(arr[0][1])
print(arr[2][2])

# Access entire row(20, 25, 29)
print(arr[1, :])

# Access entire column(19, 29, 39)
print(arr[:, 2])
