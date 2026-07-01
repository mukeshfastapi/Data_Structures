# Finding factorial number using iterative approach

def fact(n):
    accumlator = 1
    while n > 1:
        accumlator = accumlator * n
        n = n - 1
    return accumlator

print(fact(4))
