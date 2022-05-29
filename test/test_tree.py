from main.datastructures.graph.tree import Solution, minimum_depth_recursive, Node

solution = Solution()


# noinspection PyPep8Naming
def test_InOrder():
    root_node = Node(10)
    root_node.left = Node(20)
    root_node.left.left = Node(40)
    root_node.left.right = Node(60)
    root_node.right = Node(30)
    root_node.right.left = Node(50)
    actual_result = solution.InOrder(root_node)
    expected_result = [40, 20, 60, 10, 50, 30]
    assert actual_result == expected_result


# noinspection PyPep8Naming
def test_minDepth_no_root():
    actual_result = solution.minDepth(None)
    expected_result = 0
    assert actual_result == expected_result


# noinspection PyPep8Naming
def test_minDepth_right_children_only():
    root_node = Node(1)
    root_node.right = Node(2)
    root_node.right.right = Node(3)
    root_node.right.right.right = Node(4)
    actual_result = solution.minDepth(root_node)
    expected_result = 4
    assert actual_result == expected_result


# noinspection PyPep8Naming
def test_minDepth_root_only():
    root_node = Node(1)
    actual_result = solution.minDepth(root_node)
    expected_result = 1
    assert actual_result == expected_result


# noinspection PyPep8Naming
def test_minDepth_small_tree():
    root_node = Node(1)
    root_node.left = Node(3)
    root_node.left.left = Node(4)
    root_node.right = Node(2)
    actual_result = solution.minDepth(root_node)
    expected_result = 2
    assert actual_result == expected_result


# noinspection PyPep8Naming
def test_minDepth_symmetric_depth_two():
    root_node = Node(1)
    root_node.left = Node(2)
    root_node.right = Node(2)
    actual_result = solution.minDepth(root_node)
    expected_result = 2
    assert actual_result == expected_result


def test_minimum_depth_no_root():
    actual_result = minimum_depth_recursive(None)
    expected_result = 0
    assert actual_result == expected_result


def test_minimum_depth_right_children_only():
    root_node = Node(1)
    root_node.right = Node(2)
    root_node.right.right = Node(3)
    root_node.right.right.right = Node(4)
    actual_result = minimum_depth_recursive(root_node)
    expected_result = 4
    assert actual_result == expected_result


def test_minimum_depth_root_only():
    root_node = Node(1)
    actual_result = minimum_depth_recursive(root_node)
    expected_result = 1
    assert actual_result == expected_result


def test_minimum_depth_small_tree():
    root_node = Node(1)
    root_node.left = Node(3)
    root_node.left.left = Node(4)
    root_node.right = Node(2)
    actual_result = minimum_depth_recursive(root_node)
    expected_result = 2
    assert actual_result == expected_result


def test_minimum_depth_symmetric_depth_two():
    root_node = Node(1)
    root_node.left = Node(2)
    root_node.right = Node(2)
    actual_result = minimum_depth_recursive(root_node)
    expected_result = 2
    assert actual_result == expected_result
