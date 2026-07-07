# Optimized Bubble Sort
def bubble_sort(arr):
    n = len(arr)

    for i in range(n - 1):
        swapped = False

        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        # If no swapping happened, the array is already sorted
        if swapped == False:
            break

    return arr


# Driver Code
unsorted_list = [120, 25, 11, 34, 90, 22]
result = bubble_sort(unsorted_list)
print(result)