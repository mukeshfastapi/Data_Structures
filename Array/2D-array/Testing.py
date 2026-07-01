# This is a Testing file
import numpy as np

arr = np.array([[1, 2, 3], [10, 20, 30], [21, 22, 23]])

print(arr)

def search(array, target):
    for i in range(len(array)):
        for j in range(len(array[i])):
            if array[i][j] == target:
                return i, j
    return -1

print(search(arr, 1))
