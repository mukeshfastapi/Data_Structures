# Programe for sum of digits
# Like if n = 1234 output = 10

def sum_of_digits(n):
    if n == 0:
        return 0
    smallans = n % 10  # to extract the last digit ex 1234% 10 = 4
    ans = sum_of_digits(n // 10)  # removes the last digit ex= 1234// 10 = 123
    total = smallans + ans
    return total

print(sum_of_digits(1234))