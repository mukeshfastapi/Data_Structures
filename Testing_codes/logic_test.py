def logicTest(n):
    if n == 1:
        return 1
    else:
        return n + logicTest(n - 1)


print(logicTest(3))