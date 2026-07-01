# function to count the number of digits
def count_digs(n):
    res = 0  # Initializing the res = 0 bcz anything added to 0 is not going change the num

    while n > 0:
        n = n // 10
        res += 1
    return res

print(count_digs(52))
