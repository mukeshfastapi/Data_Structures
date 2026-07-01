# This is a testing environment

my_list = [10, 20, 30, 40]

def linearSearch(p_list, target):
    for i, value in enumerate(p_list):
        if value == target:
            return i

    return -1

print(linearSearch(my_list, 5))
print(linearSearch(my_list, 50))

print()

# for i, value in enumerate(my_list):
#     print(i, value)