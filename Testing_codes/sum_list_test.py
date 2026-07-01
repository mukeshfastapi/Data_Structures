# Program for sum of the list
def sum_list(l1):
    if len(l1) == 0:
        return 0
    min_ans = l1[0]
    ans = min_ans + sum_list(l1[1:])

    return ans

print(sum_list([2, 5, 8, 11]))