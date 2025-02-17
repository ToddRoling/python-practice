from src.pythonpractice.math.collection_sums import *

solution = Solution()


def test_two_sum_with_duplicates():
    list_ = [1, 2, 5, -1, 4, 4, 7, 8, 4, 9, 0]
    actual_result = two_sum(list_, 8)
    expected_result = {(-1, 9), (0, 8), (1, 7), (4, 4)}
    assert actual_result == expected_result


def test_two_sum():
    list_ = [1, 2, 5, 4, 7]
    actual_result = two_sum(list_, 9)
    expected_result = {(2, 7), (4, 5)}
    assert actual_result == expected_result


def test_all_pairs_one():
    list_a = [1, 2, 4, 5, 7]
    list_b = [5, 6, 3, 4, 8]
    actual_result = solution.allPairs(list_a, list_b, len(list_a), len(list_a), 9)
    expected_result = [(1, 8), (4, 5), (5, 4)]
    assert actual_result == expected_result


def test_all_pairs_two():
    list_a = [-1, -2, 4, -6, 5, 7]
    list_b = [6, 3, 4, 0]
    actual_result = solution.allPairs(list_a, list_b, len(list_a), len(list_a), 8)
    expected_result = [(4, 4), (5, 3)]
    assert actual_result == expected_result
