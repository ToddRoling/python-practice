from main.datastructures.graph.tree import Solution, minimum_depth_recursive, Node

solution = Solution()


def _build_medium_tree():
    root_node = Node(10)
    root_node.left = Node(20)
    root_node.left.left = Node(40)
    root_node.left.right = Node(60)
    root_node.right = Node(30)
    root_node.right.left = Node(50)
    root_node.right.left.left = Node(70)
    return root_node


def _build_right_children_only_tree():
    root_node = Node(1)
    root_node.right = Node(2)
    root_node.right.right = Node(3)
    root_node.right.right.right = Node(4)
    return root_node


def _build_small_tree():
    root_node = Node(1)
    root_node.left = Node(3)
    root_node.left.left = Node(4)
    root_node.right = Node(2)
    return root_node


def _build_symmetric_tree_depth_two():
    root_node = Node(1)
    root_node.left = Node(2)
    root_node.right = Node(2)
    return root_node


MEDIUM_TREE_ROOT_NODE = _build_medium_tree()
RIGHT_CHILDREN_ONLY_TREE_ROOT_NODE = _build_right_children_only_tree()
SMALL_TREE_ROOT_NODE = _build_small_tree()
SYMMETRIC_TREE_DEPTH_TWO_ROOT_NODE = _build_symmetric_tree_depth_two()


# noinspection PyPep8Naming
def test_height_medium_tree():
    actual_result = solution.height(MEDIUM_TREE_ROOT_NODE)
    expected_result = 4
    assert actual_result == expected_result


# noinspection PyPep8Naming
def test_height_no_root():
    actual_result = solution.height(None)
    expected_result = 0
    assert actual_result == expected_result


# noinspection PyPep8Naming
def test_height_right_children_only():
    actual_result = solution.height(RIGHT_CHILDREN_ONLY_TREE_ROOT_NODE)
    expected_result = 4
    assert actual_result == expected_result


# noinspection PyPep8Naming
def test_height_root_only():
    root_node = Node(1)
    actual_result = solution.height(root_node)
    expected_result = 1
    assert actual_result == expected_result


# noinspection PyPep8Naming
def test_height_small_tree():
    actual_result = solution.height(SMALL_TREE_ROOT_NODE)
    expected_result = 3
    assert actual_result == expected_result


# noinspection PyPep8Naming
def test_height_symmetric_tree_depth_two():
    actual_result = solution.height(SYMMETRIC_TREE_DEPTH_TWO_ROOT_NODE)
    expected_result = 2
    assert actual_result == expected_result


# noinspection PyPep8Naming
def test_InOrder():
    actual_result = solution.InOrder(MEDIUM_TREE_ROOT_NODE)
    expected_result = [40, 20, 60, 10, 70, 50, 30]
    assert actual_result == expected_result


# noinspection PyPep8Naming
def test_minDepth_no_root():
    actual_result = solution.minDepth(None)
    expected_result = 0
    assert actual_result == expected_result


# noinspection PyPep8Naming
def test_minDepth_right_children_only():
    actual_result = solution.minDepth(RIGHT_CHILDREN_ONLY_TREE_ROOT_NODE)
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
    actual_result = solution.minDepth(SMALL_TREE_ROOT_NODE)
    expected_result = 2
    assert actual_result == expected_result


# noinspection PyPep8Naming
def test_minDepth_symmetric_tree_depth_two():
    actual_result = solution.minDepth(SYMMETRIC_TREE_DEPTH_TWO_ROOT_NODE)
    expected_result = 2
    assert actual_result == expected_result


def test_minimum_depth_no_root():
    actual_result = minimum_depth_recursive(None)
    expected_result = 0
    assert actual_result == expected_result


def test_minimum_depth_right_children_only():
    actual_result = minimum_depth_recursive(RIGHT_CHILDREN_ONLY_TREE_ROOT_NODE)
    expected_result = 4
    assert actual_result == expected_result


def test_minimum_depth_root_only():
    root_node = Node(1)
    actual_result = minimum_depth_recursive(root_node)
    expected_result = 1
    assert actual_result == expected_result


def test_minimum_depth_small_tree():
    actual_result = minimum_depth_recursive(SMALL_TREE_ROOT_NODE)
    expected_result = 2
    assert actual_result == expected_result


def test_minimum_depth_symmetric_tree_depth_two():
    actual_result = minimum_depth_recursive(SYMMETRIC_TREE_DEPTH_TWO_ROOT_NODE)
    expected_result = 2
    assert actual_result == expected_result
