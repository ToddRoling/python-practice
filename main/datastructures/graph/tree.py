def minimum_depth_recursive(root):
    if not root:
        return 0

    minimum_depth = -1

    def _minimum_depth(node, current_depth):
        nonlocal minimum_depth
        current_depth += 1

        if node:
            if not (node.left or node.right):
                if minimum_depth == -1 or (current_depth < minimum_depth):
                    minimum_depth = current_depth
            else:
                _minimum_depth(node.left, current_depth)
                _minimum_depth(node.right, current_depth)

    _minimum_depth(root, 0)

    return minimum_depth


class Node:
    def __init__(self, value):
        self.right = None
        self.value = value
        self.left = None


# My solution for https://practice.geeksforgeeks.org/problems/minimum-depth-of-a-binary-tree/1/
class Solution:

    def __init__(self):
        self.minimum_depth = -1

    # noinspection PyPep8Naming
    def minDepth(self, root):
        if not root:
            return 0

        self.minimum_depth = -1

        def minimum_depth(node, current_depth):
            current_depth += 1
            if node:
                if not (node.left or node.right):
                    if self.minimum_depth == -1 or (current_depth < self.minimum_depth):
                        self.minimum_depth = current_depth
                else:
                    minimum_depth(node.left, current_depth)
                    minimum_depth(node.right, current_depth)

        minimum_depth(root, 0)

        return self.minimum_depth
