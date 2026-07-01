# program to find sum of the list using tail recursion

def sum_of_list(l1, accumlator=0):
    if not l1:  # Base condition : If list is empty then sum will be 0
        return accumlator
    ans = accumlator + l1[0]
    return ans + sum_of_list(l1[1:], accumlator)

print(sum_of_list([]))
print(sum_of_list([1, 2, 3, 4, 5]))
print(sum_of_list([10]))

