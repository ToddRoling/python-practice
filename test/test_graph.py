from main.datastructures.graph.graph import *

CYCLIC_DIRECTED_INDEX_NODE_GRAPH_ONE = [[1], [2], [3], [3]]
CYCLIC_DIRECTED_INDEX_NODE_GRAPH_TWO = [[2], [3], [4], [], [7], [1, 6], [0], [5]]
CYCLIC_DIRECTED_INDEX_NODE_GRAPH_THREE = \
    [[], [5, 6, 8, 9], [3, 7], [1], [0], [1, 4], [8, 9], [0, 1, 2], [4, 5, 7], [1, 8]]
CYCLIC_DIRECTED_INDEX_NODE_GRAPH_FOUR = [[], [0, 4], [1, 3, 4], [0, 2, 4], [0, 5], [0]]
NON_CYCLIC_DIRECTED_INDEX_NODE_GRAPH = [[4], [10], [1], [2], [5, 6], [6], [8], [0], [9], [3], []]

UNDIRECTED_CHARACTER_NODE_GRAPH = {
    'A': ['B', 'D'],
    'B': ['A', 'C', 'E'],
    'C': ['B', 'E', 'G'],
    'D': ['A', 'F'],
    'E': ['B', 'C'],
    'F': ['B', 'D'],
    'G': ['C']
}
UNDIRECTED_INDEX_NODE_GRAPH = [
    [1, 3],
    [0, 2, 4],
    [1, 4, 6],
    [0, 5],
    [1, 2],
    [1, 3],
    [2]
]

solution = Solution()


def test_bfs_iterative_character_node_graph():
    expected_result = ['A', 'B', 'D', 'C', 'E', 'F', 'G']
    actual_result = bfs_iterative_character_node_graph(UNDIRECTED_CHARACTER_NODE_GRAPH)
    assert actual_result == expected_result


def test_bfs_iterative_index_node_graph():
    expected_result = [0, 1, 3, 2, 4, 5, 6]
    actual_result = bfs_iterative_index_node_graph(UNDIRECTED_INDEX_NODE_GRAPH)
    assert actual_result == expected_result


def test_bfs_recursive_character_node_graph():
    expected_result = ['A', 'B', 'D', 'C', 'E', 'F', 'G']
    actual_result = bfs_recursive_character_node_graph(UNDIRECTED_CHARACTER_NODE_GRAPH)
    assert actual_result == expected_result


def test_bfs_recursive_index_node_graph():
    expected_result = [0, 1, 3, 2, 4, 5, 6]
    actual_result = bfs_recursive_index_node_graph(UNDIRECTED_INDEX_NODE_GRAPH)
    assert actual_result == expected_result


def test_dfs_iterative_character_node_graph():
    expected_result = ['A', 'B', 'C', 'E', 'G', 'D', 'F']
    actual_result = dfs_iterative_character_node_graph(UNDIRECTED_CHARACTER_NODE_GRAPH)
    assert actual_result == expected_result


def test_dfs_iterative_index_node_graph():
    expected_result = [0, 1, 2, 4, 6, 3, 5]
    actual_result = dfs_iterative_index_node_graph(UNDIRECTED_INDEX_NODE_GRAPH)
    assert actual_result == expected_result


def test_dfs_recursive_character_node_graph():
    # append A, B, C, E
    # pop E (via recursive function end)
    # append G
    # pop G, C, B (via recursive function end)
    # append D, F
    # pop F (via recursive function end)

    expected_result = ['A', 'B', 'C', 'E', 'G', 'D', 'F']
    actual_result = dfs_recursive_character_node_graph(UNDIRECTED_CHARACTER_NODE_GRAPH)
    assert actual_result == expected_result


def test_dfs_recursive_index_node_graph():
    expected_result = [0, 1, 2, 4, 6, 3, 5]
    actual_result = dfs_recursive_index_node_graph(UNDIRECTED_INDEX_NODE_GRAPH)
    assert actual_result == expected_result


# noinspection PyPep8Naming
def test_isCyclic_empty_array():
    actual_result = solution.isCyclic(1, [])
    expected_result = False
    assert actual_result == expected_result


# noinspection PyPep8Naming
def test_isCyclic_none_array():
    actual_result = solution.isCyclic(1, None)
    expected_result = False
    assert actual_result == expected_result


# noinspection PyPep8Naming
def test_isCyclic_zero_vertices():
    actual_result = solution.isCyclic(0, [1])
    expected_result = False
    assert actual_result == expected_result


# noinspection PyPep8Naming
def test_isCyclic_negative_vertices():
    actual_result = solution.isCyclic(-1, [1])
    expected_result = False
    assert actual_result == expected_result


# noinspection PyPep8Naming
def test_isCyclic_has_cycle_one():
    actual_result = solution.isCyclic(4, CYCLIC_DIRECTED_INDEX_NODE_GRAPH_ONE)
    expected_result = True
    assert actual_result == expected_result


# noinspection PyPep8Naming
def test_isCyclic_has_cycle_two():
    actual_result = solution.isCyclic(8, CYCLIC_DIRECTED_INDEX_NODE_GRAPH_TWO)
    expected_result = True
    assert actual_result == expected_result


# noinspection PyPep8Naming
def test_isCyclic_has_cycle_three():
    actual_result = solution.isCyclic(10, CYCLIC_DIRECTED_INDEX_NODE_GRAPH_THREE)
    expected_result = True
    assert actual_result == expected_result


# noinspection PyPep8Naming
def test_isCyclic_has_cycle_four():
    actual_result = solution.isCyclic(6, CYCLIC_DIRECTED_INDEX_NODE_GRAPH_FOUR)
    expected_result = True
    assert actual_result == expected_result


# noinspection PyPep8Naming
def test_isCyclic_has_no_cycle():
    actual_result = solution.isCyclic(11, NON_CYCLIC_DIRECTED_INDEX_NODE_GRAPH)
    expected_result = False
    assert actual_result == expected_result
