# My solution for https://practice.geeksforgeeks.org/problems/nth-node-from-end-of-linked-list/1
# noinspection PyPep8Naming
def getNthFromLast_iterative(head, n):
    if not head or n < 1:
        return -1

    leading_node = head
    trailing_node = head

    for index in range(n):
        if leading_node is None:
            return -1
        leading_node = leading_node.next

    while leading_node:
        leading_node = leading_node.next
        trailing_node = trailing_node.next

    return trailing_node.data


# My solution for https://practice.geeksforgeeks.org/problems/nth-node-from-end-of-linked-list/1
# noinspection PyPep8Naming
def getNthFromLast_recursive(head, n):
    if not head or n < 1:
        return -1

    from_last_index = 0
    result = -1

    def _get_nth_from_last(node):
        nonlocal from_last_index, result
        if node:
            _get_nth_from_last(node.next)
            from_last_index += 1
            if from_last_index == n:
                result = node.data

    _get_nth_from_last(head)
    return result


def get_singly_linked_list_middle_value(head):
    leading_node = head
    trailing_node = head

    while leading_node and leading_node.next:
        leading_node = leading_node.next.next
        trailing_node = trailing_node.next

    return trailing_node.data


def reverse_singly_linked_list_iterative(head):
    if not (head is None or head.next is None):
        current_node = head
        next_node = current_node.next
        head.next = None

        while next_node is not None:
            next_next_node = next_node.next
            next_node.next = current_node
            current_node = next_node
            next_node = next_next_node

        head = current_node

    return head


def reverse_singly_linked_list_recursive(head):
    if not (head is None or head.next is None):
        def _reverse_sll(node):
            nonlocal head
            if node.next is None:
                head.next = None
                head = node
            else:
                returned_node = _reverse_sll(node.next)
                returned_node.next = node
            return node

        _reverse_sll(head)
    return head


###

# noinspection PyPep8Naming,PyMethodMayBeStatic
class Solution:

    # My solution for https://practice.geeksforgeeks.org/problems/finding-middle-element-in-a-linked-list/1
    def findMid(self, head):
        leading_node = head
        trailing_node = head

        while leading_node and leading_node.next:
            leading_node = leading_node.next.next
            trailing_node = trailing_node.next

        return trailing_node.data


class Node:

    def __init__(self, data=0, next_node=None):
        self.data = data
        self.next = next_node


def convert_to_python_list(head):
    list_ = []
    node = head
    while node:
        list_.append(node.data)
        node = node.next
    return list_
