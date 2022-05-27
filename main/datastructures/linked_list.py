def reverse_singly_linked_list_iterative(head):
    if head is None:
        return None
    elif head.next is None:
        return head
    else:
        node = head
        next_node = node.next
        head.next = None

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
