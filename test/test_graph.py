from main.graph import *

character_node_graph = {
    'A': ['B', 'D'],
    'B': ['A', 'C', 'E'],
    'C': ['B', 'E', 'G'],
    'D': ['A', 'F'],
    'E': ['B', 'C'],
    'F': ['B', 'D'],
    'G': ['C']
}

index_node_graph = [
    [1, 3],
    [0, 2, 4],
    [1, 4, 6],
    [0, 5],
    [1, 2],
    [1, 3],
    [2]
]


def test_dfs_recursive_character_node_graph():
    # append A, B, C, E
    # pop E (via recursive function end)
    # append G
    # pop G, C, B (via recursive function end)
    # append D, F
    # pop F (via recursive function end)

    expected_result = ['A', 'B', 'C', 'E', 'G', 'D', 'F']
    actual_result = dfs_recursive_character_node_graph(character_node_graph)
    assert expected_result == actual_result


def test_dfs_recursive_index_node_graph():
    expected_result = [0, 1, 2, 4, 6, 3, 5]
    actual_result = dfs_recursive_index_node_graph(index_node_graph)
    assert expected_result == actual_result
