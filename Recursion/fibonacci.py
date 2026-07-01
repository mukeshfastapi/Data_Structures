# programme for fibonacci number

# Logic = fib(n-1) + fib( n- 2)


def fibonacci(n):
    if n == 0 or n == 1:
        return 1
    firstnum = fibonacci(n - 1)
    secnum = fibonacci(n - 2)
    ans = firstnum + secnum
    return ans

print(fibonacci(4))