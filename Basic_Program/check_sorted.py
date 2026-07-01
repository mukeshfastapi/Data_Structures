# Python Program to check if the array is sorted or not
def is_sorted(lst):
    for i in range(len(lst) - 1):  # loop will executed n - 1 check ups if 3 element in list then it should be 2 checks 
        if lst[i] > lst[i + 1]:
            return False
    return True

print(is_sorted([1, 2, 3, 4]))

print(is_sorted([1, 2, 9, 4]))
