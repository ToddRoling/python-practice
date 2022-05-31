def level_order_traversal_iterative(root):
    result = []

    if root:
        queue = [root]

        while queue:
            node = queue.pop(0)
            result.append(node)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    return result


# My solution for https://practice.geeksforgeeks.org/problems/level-order-traversal-line-by-line/1/
def level_order_traversal_level_lists_iterative(root):
    result = []

    if root:
        queue = [root]

        while queue:
            level_result = []

            for i in range(len(queue)):
                node = queue.pop(0)
                level_result.append(node.value)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            result.append(level_result)

    return result


def in_order_traversal_recursive(root):
    result = []

    def _in_order(node):
        if node:
            _in_order(node.left)
            result.append(node.value)
            _in_order(node.right)

    _in_order(root)
    return result


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


# noinspection PyMethodMayBeStatic,PyPep8Naming
class Solution:

    def __init__(self):
        self.minimum_depth = -1

    # My solution for https://practice.geeksforgeeks.org/problems/height-of-binary-tree/1
    def height(self, root):
        def _height(node):
            if node:
                return 1 + max(_height(node.left), _height(node.right))
            return 0

        return _height(root)

    # My solution for https://practice.geeksforgeeks.org/problems/inorder-traversal/1
    def InOrder(self, root):
        result = []

        def in_order(node):
            if node:
                in_order(node.left)
                result.append(node.value)
                in_order(node.right)

        in_order(root)
        return result

    # My solution for https://practice.geeksforgeeks.org/problems/minimum-depth-of-a-binary-tree/1/
    # noinspection PyMethodMayBeStatic,PyPep8Naming
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
