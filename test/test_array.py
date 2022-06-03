import pytest

from main.datastructures.array import Solution

solution = Solution()

ARRAY_MISSING_NUMBER_TEST_DATA = [
    (None, -1),
    ([1, 2, 3, 5], 4),
    ([6, 1, 2, 8, 3, 4, 7, 10, 5], 9),
    ([2], 1),
    ([1, 2, 3], 4),
    ([5, 4, 3, 2], 1),
    ([], 1)
]
MAX_SUB_ARRAY_SUM_TEST_DATA = [
    ([], None),
    ([0, 0], 0),
    ([0, 0, 1], 1),
    ([1, 0, -1], 1),
    ([1, 2, 3, -2, 5], 9),
    ([-1, -2, -3, -4], -1),
    ([-9, 900, 901, -1000, 902], 1801),
    ([0, 10, 0, -10, 0], 10),
    ([0, -10, 0, 10, 0], 10),
    ([0, -1, 0, 0, -10000, -20000], 0),
    ([93, -122, -78, 10, -9, 111, 0], 112)
]
ZIG_ZAG_TEST_DATA = [
    (None, None),
    ([], []),
    ([4, 3, 7, 8, 6, 2, 1], [3, 7, 4, 8, 2, 6, 1]),
    ([1, 4, 3, 2], [1, 4, 2, 3])
]


def test_array_equality_equal_both_empty():
    array_a = []
    array_b = []
    actual_result = solution.check(array_a, array_b, 0)
    expected_result = True
    assert actual_result == expected_result


def test_array_equality_equal_out_of_order():
    array_a = [1, 2, 5, 4, 0]
    array_b = [2, 4, 5, 0, 1]
    actual_result = solution.check(array_a, array_b, 5)
    expected_result = True
    assert actual_result == expected_result


def test_array_equality_equal_same_order():
    array_a = [1, 2, 5, 4, 0]
    array_b = [1, 2, 5, 4, 0]
    actual_result = solution.check(array_a, array_b, 5)
    expected_result = True
    assert actual_result == expected_result


def test_array_equality_unequal_same_order():
    array_a = [1, 2, 5, 4]
    array_b = [1, 2, 5, 4, 0]
    actual_result = solution.check(array_a, array_b, 5)
    expected_result = False
    assert actual_result == expected_result


def test_array_equality_equal_one_empty():
    array_a = [9, 9, 9]
    array_b = []
    actual_result = solution.check(array_a, array_b, 0)
    expected_result = False
    assert actual_result == expected_result


def test_array_equality_unequal_small():
    array_a = [1]
    array_b = [2]
    actual_result = solution.check(array_a, array_b, 5)
    expected_result = False
    assert actual_result == expected_result


# noinspection PyPep8Naming
@pytest.mark.parametrize("array, expected_result", MAX_SUB_ARRAY_SUM_TEST_DATA)
def test_maxSubArraySum(array, expected_result):
    actual_result = solution.maxSubArraySum(array, len(array))
    assert actual_result == expected_result


# noinspection PyPep8Naming
@pytest.mark.parametrize("array, expected_result", ARRAY_MISSING_NUMBER_TEST_DATA)
def test_MissingNumber(array, expected_result):
    range_upper_bound = len(array) + 1 if array is not None else 0
    actual_result = solution.MissingNumber(array, range_upper_bound)
    assert actual_result == expected_result


# noinspection PyPep8Naming
@pytest.mark.parametrize("array, expected_result", ZIG_ZAG_TEST_DATA)
def test_zigZag(array, expected_result):
    range_upper_bound = len(array) if array is not None else 0
    actual_result = solution.zigZag(array, range_upper_bound)
    assert actual_result == expected_result
