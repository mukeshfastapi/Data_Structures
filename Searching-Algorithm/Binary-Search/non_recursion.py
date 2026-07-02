# implementation of Binary Search algorithm using non recursion
# For Binary Search-- Array must have sorted
# Divide and conquer Rules

# Defining the Function
def Binary_Search(my_array, target, start, end):
    while start <= end:
        mid = start + (end-start)// 2
        if my_array[mid] == target:
            return mid
        elif my_array[mid] > target:
            end = mid -1
        else:
            start = mid +1
    return -1


# Driver code
my_array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
start = 0
end = len(my_array) - 1
target = 5

# Function calling
result = Binary_Search(my_array, target, start, end)
print(result)
