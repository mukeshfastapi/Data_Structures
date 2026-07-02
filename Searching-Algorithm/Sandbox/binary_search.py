# Implementation of Binary Search Algorithm
# Define the Function
def binary_search(arr, target):
    size = len(arr)
    start = 0
    end = size - 1

    while start <= end:
        mid = start + (end - start) // 2
        if arr[mid] == target:
            return mid

        elif arr[mid] < target:
            start = mid +1
        else:
            end = mid - 1
    return -1


# Driver code

sorted_list = [10, 23, 35, 45, 50, 70, 85]
target = 85

result = binary_search(sorted_list, target)
print(result)