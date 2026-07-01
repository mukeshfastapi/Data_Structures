# Python Program to count the number of digits

def digits_count(n):
    count = 0
    while n > 0:
        count += 1
        n = n // 10
    return count

print(digits_count(5847))










