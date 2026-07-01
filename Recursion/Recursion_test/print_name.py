# printing name n times using recursion

def printName(n):
    if n <= 0:
        return
    print('Python')
    printName(n - 1)

printName(5)