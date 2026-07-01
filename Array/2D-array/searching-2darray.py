# Searching a value in 2D Array
import numpy as np

matrix = np.array ([[10, 20, 30], [40, 50, 60], [70, 80, 90]])
print ()

print (matrix)


# Function that achive the algorithim
def search_2d_array(arr, target):
    """
    Search for a target value inside 2D Array(list of list)
    :param arr: 2D List represnting the array
    :param target: Value to search for
    :return: tuple:(row-index, col-index) if the value is found
    : -1: if the value is not found
    """
    # Loop through each row using its index
    for i in range (len (arr)):
        for j in range (len (arr[i])):  # Loop through each coulum in the current row
            if arr[i][j] == target:  # Check if the current element matches
                return i, j

    return -1
# target value
value = 50

# Function Call
result = search_2d_array(matrix, value)

# Display the result
if result != -1:
    print(f"value {value} found at the position row={result[0]}, column= {result[1]}")
else:
    print(f"value {value} not found in the 2D Array")
