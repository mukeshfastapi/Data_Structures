# Find factor number using of tail recursion
# Using of accumlator

def fact(n, accumlator=1):
    if n == 0 or n == 1:
        return accumlator

    accumlator = accumlator * n
    return fact(n - 1, accumlator)

print(fact(5))