# Programme to find the factorial of n
# Approach----> Iterative

def fact(n):
    result = 1  # Initialize with 1 bcz 0 * n return 0
    for i in range(1, n+1):  # range 1, n+1, generates numbers from 1 to n
        result = result * i
    return result

print(fact(5))