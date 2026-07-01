# Program to extract nums

def extract_num(n):
    num = n

    while num > 0:
        last_digit = num % 10
        print(last_digit)
        num = num // 10
    return last_digit

print(extract_num(4257))