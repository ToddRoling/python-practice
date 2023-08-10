def factorial_iterative(n):
    if n < 0:
        return None
    result = 1
    for i in range(n, 1, -1):
        result *= i
    return result


def factorial_recursive(n):
    if n < 0:
        return -1
    if n < 2:
        return 1
    return n * factorial_recursive(n - 1)
