# Optimize code and memory efficient
def n_to_1(n, result=None):
    if result is None:
        result = []
    if n == 0:
        return result
    result.append(n)
    return n_to_1(n - 1, result)

print(n_to_1(5))
