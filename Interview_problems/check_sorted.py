# Program to check if the array is sorted or not
# Using of recursion
def is_sorted(l1):
    if len (l1) == 0 or len (l1) == 1:  # If the list is empty of 1 element its already sorted
        return True

    if l1[0] > l1[1]:  # If the 1st element of list is greater than 2nd element then its un sorted
        return False

    return is_sorted (l1[1:])  # removes the 1st element of the lis and calls the function till the last element
    # This checks the remaining elements of the list


print (is_sorted ([2, 3, 5, 7, 9]))

l2 = [i for i in range (1000, 1, -1)]
print (is_sorted (l2))

# Important Note ⚠️
#
# This approach uses extra memory because slicing creates new lists.