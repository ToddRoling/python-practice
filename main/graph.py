def depth_first_search_iterative(graph):
    result = []
    stack = [0]
    visited_nodes = set()

    # TODO: implement
    while stack:
        ...
    #     result.append(node_index)
    #     stack.append(node_index)
    #     visited_nodes.add(node_index)
    #
    #     for element in adjacency_list[node_index]:
    #         if element not in visited_nodes:
    #             stack.append(element)
    #
    # _depth_first_search(0)

    return result


def dfs_recursive_character_node_graph(graph):
    """
    expected graph structure:
    graph = {
        'A': ['B', 'D'],
        'B': ['A', 'C', 'E'],
        'C': ['B', 'E', 'G'],
        'D': ['A', 'F'],
        'E': ['B', 'C'],
        'F': ['B', 'D'],
        'G': ['C']
    }
    """

    result = []
    visited_nodes = set()

    def _depth_first_search(node):

        result.append(node)
        visited_nodes.add(node)

        for element in graph[node]:
            if element not in visited_nodes:
                _depth_first_search(element)

    _depth_first_search(list(graph.keys())[0])

    return result


def dfs_recursive_index_node_graph(graph):
    """
    expected graph structure:
    graph = {
        [1, 3],
        [0, 2, 4],
        [1, 4, 6],
        [0, 5],
        [1, 2],
        [1, 3],
        [2]
    }
    """

    result = []
    visited_nodes = set()

    def _depth_first_search(node):

        result.append(node)
        visited_nodes.add(node)

        for element in graph[node]:
            if element not in visited_nodes:
                _depth_first_search(element)

    _depth_first_search(0)

    return result


# My solution for https://practice.geeksforgeeks.org/problems/depth-first-traversal-for-a-graph/1
class Solution:

    def __init__(self):
        self.result = []
        self.visited_nodes = set()

    # noinspection PyPep8Naming
    def dfsOfGraph(self, V, adj):

        def _depth_first_search(node):

            self.result.append(node)
            self.visited_nodes.add(node)

            for element in adj[node]:
                if element not in self.visited_nodes:
                    _depth_first_search(element)

        _depth_first_search(0)

        return self.result
