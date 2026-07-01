# creating 2D Array using numpy
import numpy as np

# creating 2D Array
arr = np.array([[1, 10, 19], [20, 25, 29], [30, 35, 39]])

print(arr)

# Updating a single value from the 2D Array (10 will replace to 11)
arr[0][1] = 11
print("After updating arr")
print(arr)
print()

# Updating the array when searching instead of indexing
pos = np.where(arr == 11)
arr[pos] = 12
print("After searching...")
print(arr)

# finding the postion of specific value in an 2DArray
pos = np.where(arr == 12)
print(pos)

# Find the value which is greater than 20
print()
grt = np.where(arr > 20)
print(grt)

# Note---->

# Visualizing
# array:
# [[ 1 10 19]
#  [20 25 29]
#  [30 35 39]]
#
# positions returned:
# (indices of values > 20)
#
# (1,1) → 25
# (1,2) → 29
# (2,0) → 30
# (2,1) → 35
# (2,2) → 39
