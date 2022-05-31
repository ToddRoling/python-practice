import pytest

from main.datastructures.graph.graph import *

DIRECTED_INDEX_NODE_GRAPH_TEST_DATA = [
    ([[1], [2], [3], [3]], True),
    ([[2], [3], [4], [], [7], [1, 6], [0], [5]], True),
    ([[], [5, 6, 8, 9], [3, 7], [1], [0], [1, 4], [8, 9], [0, 1, 2], [4, 5, 7], [1, 8]], True),
    ([[], [0, 4], [1, 3, 4], [0, 2, 4], [0, 5], [0]], True),
    ([[4], [10], [1], [2], [5, 6], [6], [8], [0], [9], [3], []], False),
]
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
    expected_result = ['A', 'B', 'C', 'E', 'G', 'D', 'F']
    actual_result = dfs_recursive_character_node_graph(UNDIRECTED_CHARACTER_NODE_GRAPH)
    assert actual_result == expected_result


def test_dfs_recursive_index_node_graph():
    expected_result = [0, 1, 2, 4, 6, 3, 5]
    actual_result = dfs_recursive_index_node_graph(UNDIRECTED_INDEX_NODE_GRAPH)
    assert actual_result == expected_result


###


# noinspection PyPep8Naming
@pytest.mark.parametrize("directed_index_node_graph, expected_result", DIRECTED_INDEX_NODE_GRAPH_TEST_DATA)
def test_isCyclic(directed_index_node_graph, expected_result):
    actual_result = solution.isCyclic(len(directed_index_node_graph), directed_index_node_graph)
    assert actual_result == expected_result


# noinspection PyPep8Naming
def test_isCyclic_empty_array():
    actual_result = solution.isCyclic(1, [])
    expected_result = False
    assert actual_result == expected_result


# noinspection PyPep8Naming
def test_isCyclic_negative_vertices():
    actual_result = solution.isCyclic(-1, [1])
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
