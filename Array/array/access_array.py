# Accessing the array elements
from array import *

my_arr = array('i', [12, 25, 28, 30])

print(my_arr)

# Traditional approach of accessing value
def accessElement(arr, index):
    if index >= len(arr):
        print('There is No elements in this range')
    else:
        print(arr[index])

# Invoking the Function
accessElement(my_arr, 5)

# calling function with a valid range
accessElement(my_arr, 3)

# accessing Elements with safe-access
def safe_acess(arr, index):
    try:
        return arr[index]
    except IndexError:
        return f"Error: Valid index range is 0 to {len(arr)-1}"

# Invoking the Function
print(safe_acess(my_arr, 9))

# Invoking with the valid index
print(safe_acess(my_arr, 2))
