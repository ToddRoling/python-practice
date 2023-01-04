# My solution to https://www.hackerrank.com/challenges/py-if-else/problem
# noinspection PyPep8Naming,PyMethodMayBeStatic
def print_weirdness(n):
    is_weird = (n % 2 != 0) or (n in range(6, 21))
    if not is_weird:
        print("Not ", end='')
    print("Weird")
