import pytest

from src.pythonpractice.datastructures.array import Solution

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
ROTATE_ARRAY_CCW_TEST_DATA = [
    ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[3, 6, 9], [2, 5, 8], [1, 4, 7]]),
    ([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]],
     [[4, 8, 12, 16], [3, 7, 11, 15], [2, 6, 10, 14], [1, 5, 9, 13]]),
    ([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 25]],
     [[5, 10, 15, 20, 25], [4, 9, 14, 19, 24], [3, 8, 13, 18, 23], [2, 7, 12, 17, 22], [1, 6, 11, 16, 21]]),
    ([[1, 2, 3, 4, 5, 6], [7, 8, 9, 10, 11, 12], [13, 14, 15, 16, 17, 18], [19, 20, 21, 22, 23, 24],
      [25, 26, 27, 28, 29, 30], [31, 32, 33, 34, 35, 36]],
     [[6, 12, 18, 24, 30, 36], [5, 11, 17, 23, 29, 35], [4, 10, 16, 22, 28, 34], [3, 9, 15, 21, 27, 33],
      [2, 8, 14, 20, 26, 32], [1, 7, 13, 19, 25, 31]])
]
ROTATED_ARRAY_SEARCH_TEST_DATA = [
    ([5, 6, 7, 8, 9, 10, 1, 2, 3], 10, 5),
    ([3, 5, 1, 2], 6, -1),
    ([6, 18, -999, -45, -1, 0, 4, 5], 6, 0),
    ([6, 18, -999, -45, -1, 0, 4, 5], -45, 3)
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


@pytest.mark.parametrize("array, expected_result", ROTATE_ARRAY_CCW_TEST_DATA)
def test_rotate_matrix_ccw(array, expected_result):
    actual_result = solution.rotateMatrix(array, len(array))
    assert actual_result == expected_result


@pytest.mark.parametrize("array, key, expected_result", ROTATED_ARRAY_SEARCH_TEST_DATA)
def test_search(array, key, expected_result):
    actual_result = solution.search(array, 0, len(array) - 1, key)
    assert actual_result == expected_result


# noinspection PyPep8Naming
@pytest.mark.parametrize("array, expected_result", ZIG_ZAG_TEST_DATA)
def test_zigZag(array, expected_result):
    range_upper_bound = len(array) if array is not None else 0
    actual_result = solution.zigZag(array, range_upper_bound)
    assert actual_result == expected_result
