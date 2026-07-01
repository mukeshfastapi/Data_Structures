# def num_add(nm):
#     print(nm)
#     if nm == 1:
#         return
#     num_add(nm - 2)
#
#
# num_add(5)

# n = 10
# for i in range(n, -1, -1):
#     print(i)

def fact(n):
    if n == 0:
        return 1
    smallans = fact(n-1)
    return smallans

print(fact(5))