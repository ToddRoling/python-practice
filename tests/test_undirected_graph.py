from src.pythonpractice.datastructures.graph.undirected_graph import *

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
