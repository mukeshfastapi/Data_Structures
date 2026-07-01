# Creating a python buit in array
import array
from array import *

my_arr = array('i', [12, 23, 25])
print(my_arr)

# creating a string array
char_array = array('u', "Python")

# creating a float array
float_array = array('f', [1.5])

print(my_arr, char_array, float_array)

# Note--> In python built in array you cannot store a whole string using typecode-'u'
# ['python'] 