# This program find the greatest between two number
def largest(a, b):
    return a if a > b else b

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

print("Largest number:", largest(x, y))