"""
expected index-node graph (adjacency list) structure format:
e.g. graph = [[1], [2], [3], [3]]
e.g. graph = [[2], [3], [4], [], [7], [1, 6], [0], [5]]
e.g. graph = [[], [5, 6, 8, 9], [3, 7], [1], [0], [1, 4], [8, 9], [0, 1, 2], [4, 5, 7], [1, 8]]
e.g. graph = [[], [0, 4], [1, 3, 4], [0, 2, 4], [0, 5], [0]]
e.g. graph = [[4], [10], [1], [2], [5, 6], [6], [8], [0], [9], [3], []]
"""


# noinspection PyPep8Naming,PyMethodMayBeStatic
class Solution:

    # My solution for https://practice.geeksforgeeks.org/problems/detect-cycle-in-a-directed-graph/1
    # Function to detect cycle in a directed graph.
    def isCyclic(self, V, adj):
        if not adj or V <= 0:
            return False

        ancestor_nodes = [False] * V
        visited_nodes = [False] * V

        def _is_cyclic(node):
            ancestor_nodes[node] = True
            visited_nodes[node] = True

            for child in adj[node]:
                if ancestor_nodes[child]:
                    # Back edge if node's child is also an ancestor
                    return True
                if not visited_nodes[child]:
                    if _is_cyclic(child):
                        return True

            ancestor_nodes[node] = False
            return False

        for root in range(V):
            if not visited_nodes[root]:
                if _is_cyclic(root):
                    return True
        return False
