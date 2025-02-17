from src.pythonpractice.strings.longest_common_prefix import Solution

solution = Solution()


# noinspection PyPep8Naming
def test_longestCommonPrefix_found():
    array = ["geeksforgeeks", "geeks", "geek", "geezer"]
    actual_result = solution.longestCommonPrefix(array, len(array))
    expected_result = "gee"
    assert actual_result == expected_result


# noinspection PyPep8Naming
def test_longestCommonPrefix_not_found():
    array = ["hello", "world"]
    actual_result = solution.longestCommonPrefix(array, len(array))
    expected_result = -1
    assert actual_result == expected_result


# noinspection PyPep8Naming
def test_longestCommonPrefix_found_one_character():
    array = ["h", "he", "h", "hey"]
    actual_result = solution.longestCommonPrefix(array, len(array))
    expected_result = "h"
    assert actual_result == expected_result


# noinspection PyPep8Naming
def test_longestCommonPrefix_none_array():
    array = None
    actual_result = solution.longestCommonPrefix(array, 0)
    expected_result = -1
    assert actual_result == expected_result


# noinspection PyPep8Naming
def test_longestCommonPrefix_one_empty_string():
    array = [""]
    actual_result = solution.longestCommonPrefix(array, 0)
    expected_result = -1
    assert actual_result == expected_result


# noinspection PyPep8Naming
def test_longestCommonPrefix_one_nonempty_string():
    array = ["hello"]
    actual_result = solution.longestCommonPrefix(array, 0)
    expected_result = "hello"
    assert actual_result == expected_result


# noinspection PyPep8Naming
def test_longestCommonPrefix_two_empty_strings():
    array = ["", ""]
    actual_result = solution.longestCommonPrefix(array, 0)
    expected_result = -1
    assert actual_result == expected_result
