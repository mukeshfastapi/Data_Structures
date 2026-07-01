# array insertion opeartions
from array import *

my_arr = array('i', [12, 25, 28, 30])

# Before insertion elements
print(my_arr)

# insert--> syntax-->insert(pos,val)
my_arr.insert(0, 45)
print(f'After insertion {my_arr}')

# inserting middle of the array
my_arr.insert(2, 55)
print()
print(f'After insertion in the middle of the array {my_arr}')

# inserting last in the array
my_arr.insert(6, 100)
print()
print(f'After insertion in the last of the array {my_arr}')