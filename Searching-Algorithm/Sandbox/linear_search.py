# Program to find an Element from a list
# suppose my list is like [10, 23, 45, 70, 11]
# Need a program to find 70 , if it is present return 1 or return -1

"""
  Begin
 create a Function that will take 2 parameters:
traverse the list using a for loop:
if item found in the list: return the index
else return -1

 end
"""
def linear_search(arr, target):
    size = len(arr)
    for i in range(size):
        if arr[i] == target:
            return i
    return -1

tar_list = [10, 23, 45, 70, 11]
target = 100
result = linear_search(tar_list, target)

print(result)

tar_list = [10, 23, 45, 70, 11]
target = 70
result = linear_search(tar_list, target)
print(result)