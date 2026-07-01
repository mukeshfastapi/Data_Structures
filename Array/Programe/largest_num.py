# Python program to find the largest number in an array

# Using sorting
arr = [10, 25, 3, 99, 56, 70]

# arr.sort()
# print(arr)
# print("The largest number is:", arr[-1])

# Using max()
# print("Largest number is:", max(arr))

# using a Loop

# Create a function
def find_largest(array):
    # "assume 1st number is largest"
    largest = arr[0]
    # Traverse the array value (not index like range(len(array))
    for num in array:
        if num > largest:
            largest = num
    return largest

print(find_largest(arr))

