# python problem to find sum of n natural nums

# if n = 5 then sum of n  is 5+4+3+2+1
# sum = n -1(n-2)...1
# n = sum(n-1)
def sum_of_till_n(n):
    if n == 1:
        return 1
    smallans = sum_of_till_n(n - 1)
    ans = n + smallans
    return ans

print(sum_of_till_n(5))