# implementation of Binary Search algorithm using recursion
# For Binary Search-- Array must have sorted
# Divide and conquer Rules

# Defining the Function
def Binary_Search(arr, target, start, end):
    while start <= end:
        mid = start + (end - start) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            return Binary_Search(arr, target, mid + 1, end)

        else:
            return Binary_Search(arr, target, start, mid - 1)
    return -1

# Driver Code
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
target = 10
start = 0
end = len(arr)-1

# Function Calling
result = Binary_Search(arr, target, start, end)
print(result)