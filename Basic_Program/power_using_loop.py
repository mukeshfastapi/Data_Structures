# find the power using of loops inside function
def power(n, p):

    result = 1
    for i in range(p):
        result *= n  # each time loop execute and multiply with n

    return result

print(power(5, 2))

