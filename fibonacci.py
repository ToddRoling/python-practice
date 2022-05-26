def print_fibonacci(depth):
    a, b = 0, 1
    print(f"{a}, {b}", end='')
    for i in range(depth - 2):
        temp = a
        a = b
        b += temp
        print(f", {b}", end='')
    print()

