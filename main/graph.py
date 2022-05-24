def depth_first_search_iterative(adjacency_list):

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


def depth_first_search_recursive(adjacency_list):

    result = []
    visited_nodes = set()

    def _depth_first_search(node_index):

        result.append(node_index)
        visited_nodes.add(node_index)

        for element in adjacency_list[node_index]:
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

        def _depth_first_search(node_index):

            self.result.append(node_index)
            self.visited_nodes.add(node_index)

            for element in adj[node_index]:
                if element not in self.visited_nodes:
                    _depth_first_search(element)

        _depth_first_search(0)

        return self.result
