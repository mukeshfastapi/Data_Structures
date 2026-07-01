# Python programme to find the missing  number in an List

my_arr = [1, 2, 4, 5, 6]

# Total number in this sequence should be 6

n = 6

# function to find
def missing_num(arr, n):  # Function takes 2 param -> 1- My array , 2- sequnce of total num n
    # # Calculate the sum of first n natural numbers
    total_sum = n * (n+1) // 2
    arr_sum = sum(arr)  # Total sum of existing array
    mising_value = total_sum - arr_sum  # differences is the missing number
    return mising_value

# Invoking the Function
print("Missing Value in the sequnece is :", missing_num(my_arr, n))