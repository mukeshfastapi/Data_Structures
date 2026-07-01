# program to find sum of the list using recursion
def sum_of_list(l1):
    if len(l1) == 0:
        return 0

    ans = l1[0] + sum_of_list(l1[1:])
    return ans

print(sum_of_list([]))

print(sum_of_list([1, 2, 3, 4]))
