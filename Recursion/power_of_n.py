# Program for 2 power of n
# def power_of_n(n):
#     if n == 1:
#         return 2
#     smallans = power_of_n(n - 1)
#     ans = 2 * smallans
#     return ans
#
# print(power_of_n(5))

# program for 2 power of n if it is nagative
def power_of_two(n):
    if n == 1:
        return 2
    elif n > 0:
        return 2 * power_of_two(n-1)
    else:
        return 0.5 * power_of_two(n + 1)

print(power_of_two(-3))
print(power_of_two(3))