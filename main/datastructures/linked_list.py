class Node:
    # noinspection PyShadowingBuiltins
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


# My implementation of LinkedList for practice
class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def _get_middle_node(self):
        leading_node = self.head
        trailing_node = self.head

        while leading_node and leading_node.next:
            leading_node = leading_node.next.next
            trailing_node = trailing_node.next

        return trailing_node

    def _get_node(self, index):
        if index > self.size - 1:
            self._raise_index_range_error()
        counter = 0
        node = self.head
        while counter < index:
            node = node.next
            counter += 1
        return node

    def _raise_index_range_error(self):
        raise IndexError("index is out of range")

    # appends a new node containing data at end of list
    def append(self, data):
        new_node = Node(data)
        if self.size == 0:
            self.head = new_node
        else:
            self.tail.next = new_node
        self.tail = new_node
        self.size += 1

    def get(self, index):
        return self._get_node(index).data

    def get_last(self):
        return self.tail.data

    def get_mid(self):
        return self._get_middle_node().data

    # inserts a new node containing data before index
    def insert(self, index: int, data):
        if index > self.size - 1:
            self._raise_index_range_error()
        new_node = Node(data)
        if index == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            previous_node = self._get_node(index - 1)
            next_node = previous_node.next
            previous_node.next = new_node
            new_node.next = next_node
        self.size += 1

    # TODO: implement
    def remove(self):
        ...

    # TODO: implement
    def remove_last(self):
        ...

    # TODO: implement
    def sort(self):
        ...

    def reverse(self):
        if not (self.head is None or self.head.next is None):

            current_node = self.head
            next_node = current_node.next

            self.tail = self.head
            self.tail.next = None

            while next_node is not None:
                next_next_node = next_node.next
                next_node.next = current_node
                current_node = next_node
                next_node = next_next_node

            self.head = current_node

        return self.head
