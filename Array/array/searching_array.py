# Searching an element in array
from array import *

my_arr = array('i', [12, 25, 28, 30, 99])

print(my_arr)

# Function to search manually an elements in array
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

# invoking the function
print(linear_search(my_arr, 99))

# something not in array
print(linear_search(my_arr, 100))

def linear_search(arr, target):
    for i in range(len(arr)):
        if i == target:
            return i
    return -1

# invoking the function
print(linear_search(my_arr, 99))


# Testing
print('Testing.............')
ar = array('i', [10,11,21])
for i in range(len(ar)):
    print(i)

for i in range(len(ar)):
    print(ar[i])