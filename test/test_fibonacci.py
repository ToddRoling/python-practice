import pytest

from main.math.fibonacci import *

TEST_DATA_NTH_SEQUENCE = (
    (0, []),
    (1, [0]),
    (2, [0, 1]),
    (3, [0, 1, 1]),
    (5, [0, 1, 1, 2, 3]),
    (7, [0, 1, 1, 2, 3, 5, 8]),
    (11, [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55])
)
TEST_DATA_NTH_TERM = ((0, 0), (1, 1), (2, 1), (5, 5), (11, 89), (19, 4181))


@pytest.mark.parametrize("n, expected_result", TEST_DATA_NTH_TERM)
def test_fibonacci_iterative(n, expected_result):
    actual_result = fibonacci_iterative(n)
    assert actual_result == expected_result


@pytest.mark.parametrize("n, expected_result", TEST_DATA_NTH_TERM)
def test_fibonacci_recursive(n, expected_result):
    actual_result = fibonacci_recursive(n)
    assert actual_result == expected_result


@pytest.mark.parametrize("n, expected_result", TEST_DATA_NTH_SEQUENCE)
def test_fibonacci_sequence_recursive(n, expected_result):
    actual_result = fibonacci_sequence_recursive(n)
    assert actual_result == expected_result
