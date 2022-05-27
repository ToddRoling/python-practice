# return nth fibonacci term
def fibonacci_iterative(n):
    if n < 2:
        return n
    a, b = 0, 1
    for i in range(1, n):
        sum_ = a + b
        a = b
        b = sum_
    return b


# return nth fibonacci term
def fibonacci_recursive(n):
    if n <= 1:
        return n
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


# return first n fibonacci terms as list where n == 1 returns [0]
def fibonacci_sequence_recursive(n):
    a, b = 0, 1
    result = [a, b]

    if n == 0:
        return []
    if n == 1:
        return [0]
    if n == 2:
        return result

    def _fibonacci_sequence(remaining_terms):
        nonlocal a, b

        if remaining_terms == 0:
            return result

        sum_ = a + b
        a = b
        b = sum_
        result.append(sum_)
        _fibonacci_sequence(remaining_terms - 1)

    _fibonacci_sequence(n - 2)
    return result


def print_fibonacci_sequence(n):
    a, b = 0, 1
    print(f"{a}, {b}", end='')
    for i in range(n - 2):
        sum_ = a
        a = b
        b += sum_
        print(f", {b}", end='')
    print()
