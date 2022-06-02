import pytest

from main.sort.sort import Solution

SORT_012_TEST_DATA = [
    (None, None),
    ([0, 2, 1, 2, 0], [0, 0, 1, 2, 2]),
    ([0, 1, 0], [0, 0, 1]),
    ([], []),
    ([1, 0, 2], [0, 1, 2]),
    ([2, 0, 1], [0, 1, 2]),
    ([1, 2, 0, 1], [0, 1, 1, 2]),
    ([1, 2, 2, 0], [0, 1, 2, 2]),
    ([2, 1, 2, 0], [0, 1, 2, 2])
]

solution = Solution()


@pytest.mark.parametrize("array, expected_result", SORT_012_TEST_DATA)
def test_sort012_v0(array, expected_result):
    n = len(array) if array is not None else None
    actual_result = solution.sort012_v0(array, n)
    assert actual_result == expected_result


@pytest.mark.parametrize("array, expected_result", SORT_012_TEST_DATA)
def test_sort012_v1(array, expected_result):
    n = len(array) if array is not None else None
    actual_result = solution.sort012_v1(array, n)
    assert actual_result == expected_result
