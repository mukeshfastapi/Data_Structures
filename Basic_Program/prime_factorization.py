# Prime ----> Factorization

def isPrime(n):
    if n <= 1:
        return False

    for i in range (2, int (n ** 0.5) + 1):
        if n % i == 0:  # FIXED: check divisibility by i, not 2
            return False

    return True


def Prime_Factor(x):
    for i in range (2, x + 1):
        if isPrime (i):
            while x % i == 0:
                print (i)
                x = x // i  # FIXED: divide instead of multiply


n = int (input ("Enter n: "))

Prime_Factor (n)  # FIXED: removed print()


