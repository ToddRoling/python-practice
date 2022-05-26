"""
expected character-node graph structure:
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

"""
expected index-node graph structure:
graph = [
    [1, 3],
    [0, 2, 4],
    [1, 4, 6],
    [0, 5],
    [1, 2],
    [1, 3],
    [2]
]
"""


def _breadth_first_search_iterative(graph, root_node):
    if not graph:
        return graph

    queue = [root_node]
    result = [root_node]
    visited_nodes = {root_node}

    while queue:
        _visit_adjacent_nodes(graph, queue, result, visited_nodes)

    return result


def _breadth_first_search_recursive(graph, root_node):
    if not graph:
        return graph

    queue = [root_node]
    result = [root_node]
    visited_nodes = {root_node}

    def _breadth_first_search():
        if queue:
            _visit_adjacent_nodes(graph, queue, result, visited_nodes)
            _breadth_first_search()

    _breadth_first_search()

    return result


def _visit_adjacent_nodes(graph, queue, result, visited_nodes):
    node = queue.pop(0)

    for adjacent_node in graph[node]:
        if adjacent_node not in visited_nodes:
            queue.append(adjacent_node)
            result.append(adjacent_node)
            visited_nodes.add(adjacent_node)


def _depth_first_search_iterative(graph, root_node):
    if not graph:
        return graph

    result = []
    stack = [root_node]
    visited_nodes = set()

    while stack:

        node = stack.pop()
        if node not in visited_nodes:

            visited_nodes.add(node)
            result.append(node)

            adjacency_list = graph[node]
            for adjacent_node in adjacency_list[-1::-1]:
                stack.append(adjacent_node)

    return result


def _depth_first_search_recursive(graph, root_node):
    if not graph:
        return graph

    result = []
    visited_nodes = set()

    def _depth_first_search(node):
        result.append(node)
        visited_nodes.add(node)

        for adjacent_node in graph[node]:
            if adjacent_node not in visited_nodes:
                _depth_first_search(adjacent_node)

    _depth_first_search(root_node)

    return result


def bfs_iterative_index_node_graph(graph):
    return _breadth_first_search_iterative(graph, 0)


def bfs_iterative_character_node_graph(graph):
    root_node = list(graph.keys())[0]
    return _breadth_first_search_iterative(graph, root_node)


def bfs_recursive_index_node_graph(graph):
    return _breadth_first_search_recursive(graph, 0)


def bfs_recursive_character_node_graph(graph):
    root_node = list(graph.keys())[0]
    return _breadth_first_search_recursive(graph, root_node)


def dfs_iterative_character_node_graph(graph):
    root_node = list(graph.keys())[0]
    return _depth_first_search_iterative(graph, root_node)


def dfs_iterative_index_node_graph(graph):
    return _depth_first_search_iterative(graph, 0)


def dfs_recursive_character_node_graph(graph):
    root_node = list(graph.keys())[0]
    return _depth_first_search_recursive(graph, root_node)


def dfs_recursive_index_node_graph(graph):
    return _depth_first_search_recursive(graph, 0)


class Solution:

    def __init__(self):
        self.queue = []
        self.result = []
        self.visited_nodes = set()

    # My solution for https://practice.geeksforgeeks.org/problems/bfs-traversal-of-graph/1
    # noinspection PyPep8Naming
    def bfsOfGraph(self, V, adj):

        self.queue = [0]
        self.result = [0]
        self.visited_nodes = {0}

        def _breadth_first_search():
            if self.queue:
                node = self.queue.pop(0)
                for adjacent_node in adj[node]:
                    if adjacent_node not in self.visited_nodes:
                        self.queue.append(adjacent_node)
                        self.result.append(adjacent_node)
                        self.visited_nodes.add(adjacent_node)

                _breadth_first_search()

        _breadth_first_search()

        return self.result

    # My solution for https://practice.geeksforgeeks.org/problems/depth-first-traversal-for-a-graph/1
    # noinspection PyPep8Naming
    def dfsOfGraph(self, V, adj):

        self.result = []
        self.visited_nodes = set()

        def _depth_first_search(node):

            self.result.append(node)
            self.visited_nodes.add(node)

            for adjacent_node in adj[node]:
                if adjacent_node not in self.visited_nodes:
                    _depth_first_search(adjacent_node)

        _depth_first_search(0)

        return self.result
