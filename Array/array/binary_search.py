# Introducing Binary Search Algorithm(Recursive Approach)

# Function definition
def BinarySearch(arr, i, j, x):
    while i <= j:
        mid = i + (j-i)//2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            return BinarySearch(arr, mid+1, j, x)
        else:
            return BinarySearch(arr, mid-1, i, x)
    else:
        return -1

arr = [10, 20, 30, 45, 55, 65, 95]
i = 0
j = len(arr) -1
x = 65

result = BinarySearch(arr, i, j, x)

print(f'Found in index:', result)