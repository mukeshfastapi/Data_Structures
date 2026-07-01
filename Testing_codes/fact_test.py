def fact(n):
    if n == 0 or n == 1:
        return 1

    smallans = fact(n - 1)
    ans = n * smallans
    return ans

print(fact(5))