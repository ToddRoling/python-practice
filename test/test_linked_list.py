import pytest

from main.datastructures.linked_list import *

NODE_DATA_LIST_EVEN_LENGTH = ['a', 'b', 'c', 'd', 'e', 'f']
NODE_DATA_LIST_ODD_LENGTH = ['a', 'b', 'c', 'd', 'e']
NODE_DATA_LIST_ODD_LENGTH_REVERSED = ['e', 'd', 'c', 'b', 'a']


@pytest.fixture()
def create_linked_list_even_length():
    return create_linked_list(NODE_DATA_LIST_EVEN_LENGTH)


@pytest.fixture()
def create_linked_list_odd_length():
    return create_linked_list(NODE_DATA_LIST_ODD_LENGTH)


def create_linked_list(list_):
    head = Node(list_[0])
    node = head
    for element in list_[1:]:
        node.next = Node(element)
        node = node.next
    return head


def test_find_mid_even_length(create_linked_list_even_length):
    linked_list_head = create_linked_list_even_length
    expected_result = 'd'
    actual_result = get_singly_linked_list_middle_value(linked_list_head)
    assert actual_result == expected_result


def test_find_mid_odd_length(create_linked_list_odd_length):
    linked_list_head = create_linked_list_odd_length
    expected_result = 'c'
    actual_result = get_singly_linked_list_middle_value(linked_list_head)
    assert actual_result == expected_result


# noinspection PyPep8Naming
def test_findMid(create_linked_list_odd_length):
    linked_list_head = create_linked_list_odd_length
    expected_result = 'c'
    actual_result = Solution().findMid(linked_list_head)
    assert actual_result == expected_result


def test_reverse_singly_linked_list_iterative(create_linked_list_odd_length):
    linked_list_head = create_linked_list_odd_length
    expected_result = NODE_DATA_LIST_ODD_LENGTH_REVERSED
    actual_result = reverse_singly_linked_list_iterative(linked_list_head)
    actual_result = convert_to_python_list(actual_result)
    assert actual_result == expected_result


def test_reverse_singly_linked_list_recursive(create_linked_list_odd_length):
    linked_list_head = create_linked_list_odd_length
    expected_result = NODE_DATA_LIST_ODD_LENGTH_REVERSED
    actual_result = reverse_singly_linked_list_recursive(linked_list_head)
    actual_result = convert_to_python_list(actual_result)
    assert actual_result == expected_result
