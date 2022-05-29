from main.datastructures.array import Solution

solution = Solution()


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
