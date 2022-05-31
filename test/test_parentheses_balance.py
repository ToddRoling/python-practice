import pytest

from main.parentheses_balance import Solution

solution = Solution()

TEST_DATA = [
    ("", True),
    ("[", False),
    ("[]", True),
    ("]", False),
    ("[[", False),
    ("]]", False),
    ("[[]", False),
    ("[]]", False),
    ("[[]]", True),
    ("(]", False),
    ("{)", False),
    ("{}", True),
    ("()", True),
    ("({)}", False),
    ("({)[}]", False),
    ("({[}])", False),
    ("({}[])", True),
    ("a(  [])8jj3{}", True),
    ("a(  [)8jj3{}", False),
]


@pytest.mark.parametrize("string, expected_result", TEST_DATA)
def test_parentheses_balance(string, expected_result):
    actual_result = solution.ispar(string)
    assert actual_result == expected_result
