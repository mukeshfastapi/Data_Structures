# Check the list is sorted
def is_sorted(l1):
    if len(l1) <= 1:
        return True
    if l1[0] > l1[1]:
        return False
    return is_sorted(l1[1:])

print(is_sorted([2, 3, 5, 7, 9]))