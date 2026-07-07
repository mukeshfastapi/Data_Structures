# Implementation of Selection Sort
# Defining the function
def selection_sort(arr):
    n = len(arr)
    for i in range(n-1):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr

# Driver code
unsorted_list = [120, 25, 11, 34, 90, 22]
result = selection_sort(unsorted_list)
print(result)