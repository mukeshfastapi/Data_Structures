#$  programme to find the sum of digits

def sum_of(n):
    if n == 0:
        return 0

    s_ans = n % 10
    ans = sum_of(n // 10)
    total = s_ans + ans
    return total

print(sum_of(456))