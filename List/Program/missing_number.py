# Python programme to find the missing  number in an List


# if the number from 1 to n is complete the sum shpuld be
# sum = n(n+1)/2
# 6*7/2 =21
#
# but here sum = 1 +2+4+5+6= 18
# missing  num = 21-18= 3


def find_missing(ar, n):
    total_sum = n * (n+1) // 2
    arr_sum = sum(ar)
    return total_sum - arr_sum

# Given Array
arr = [1, 2, 4, 5, 6]
n = 6

print("Missing number is:", find_missing(arr, n))
