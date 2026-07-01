# Function to find the power of n , Eg:
#
# User will give 2 inputs 1 is base and 2nd is power
# Suppose user enter 5 as base and 2 as power , then output should be 25

def power_of(base, power):
    return base ** power

print(power_of(5, 2))

# Using of one line Approach: lambda
power = lambda n, p: n ** p
print(power(5, 3))