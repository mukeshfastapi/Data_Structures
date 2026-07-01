# Program to find the power of nth , Eg: N = 5, P = 3 op--> 125

def power_of_n(base, power):
    if power == 0:
        return 1

    power_n = power_of_n(base, power - 1)
    return base * power_n

print(power_of_n(5, 3))
print(power_of_n(2, 3))
