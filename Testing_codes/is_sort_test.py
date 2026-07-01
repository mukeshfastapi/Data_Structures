# # testing a list / array if it is sorted
# def is_sorted(l1):
#     if len (l1) == 0 or len (l1) == 1:
#         return True
#
#     if l1[0] < l1[1]:
#         return is_sorted (l1[1:])
#
#     else:
#         return False
#
#
# print (is_sorted ([2, 3, 5, 7]))
# print (is_sorted ([2, 3, 11, 7]))
# print(is_sorted([]))
# print(is_sorted([11]))
def is_sorted(l1):
    if len(l1)<= 1:
        return True

    if l1[0] > l1[1]:
        return False
    return is_sorted(l1[1:])

print (is_sorted ([2, 3, 5, 7]))
print (is_sorted ([2, 3, 11, 7]))
print(is_sorted([]))
print(is_sorted([11]))


