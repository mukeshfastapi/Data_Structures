# Deleting element from an array
from array import *

my_arr = array('i', [12, 25, 28, 30, 99])

print(my_arr)

# Function to delete elements from an array
def delete_element(arr, target):
    if target in arr:
        arr.remove(target)
        return f"{target} removed sucessfully from the Array"
    else:
        return f"{target}  not found in the Array"

print(delete_element(my_arr, 500))

my_arr1 = array('i', [500, 700, 900, 100])

# Testing of using Pop method to delete item in an array
def delete_pop(arr, value):
    if value in arr:
        index = arr.index(value)
        popping = arr.pop(index)
        print(f"popping item is {popping} ")
    else:
        print('Item not found')

delete_pop(my_arr1, 100)
delete_pop(my_arr1, 500)
