def reverse_singly_linked_list_iterative(head):
    if head is None:
        return None
    elif head.next is None:
        return head
    else:
        return reverse_sll_iterative_helper(head)


def reverse_sll_iterative_helper(node):
    next_node = node.next
    node.next = None

    while next_node is not None:
        next_next_node = next_node.next
        next_node.next = node
        node = next_node
        next_node = next_next_node

    return node


def reverse_singly_linked_list_recursive(head):
    if head is None:
        return None
    elif head.next is None:
        return head
    else:
        return reverse_sll_recursive_helper(head)[0]


def reverse_sll_recursive_helper(node):
    if node.next is None:
        head = node
    else:
        result = reverse_sll_recursive_helper(node.next)
        head = result[0]
        returned_node = result[1]
        returned_node.next = node
        node.next = None
    return head, node
