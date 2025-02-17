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
        if not adj or V <= 0 or len(adj) != V:
            return False

        ancestor_nodes = set()
        visited_nodes = set()

        def _is_cyclic(node):
            ancestor_nodes.add(node)
            visited_nodes.add(node)

            for child in adj[node]:
                if child in ancestor_nodes:
                    # Back edge if node's child is also an ancestor
                    return True
                if child not in visited_nodes:
                    if _is_cyclic(child):
                        return True

            ancestor_nodes.remove(node)
            return False

        for root in range(V):
            if root not in visited_nodes:
                if _is_cyclic(root):
                    return True
        return False
