# Traversing the array---> reading  each value in the array
from array import *

my_arr = array('i', [12, 25, 28, 30])

# Traversing the entire array
for i in my_arr:
    print(i)

# Traversing index wise
print()

for i in range(len(my_arr)):
    print(my_arr[i])

# Traversing using while loops
print("Traversing using while loop---")
i = 0
while i < len(my_arr):
    print(my_arr[i])
    i += 1
