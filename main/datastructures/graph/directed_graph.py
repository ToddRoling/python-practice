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
                if not visited_nodes[child]:
                    if _is_cyclic(child):
                        return True
                if ancestor_nodes[child]:
                    # Back edge if node's child is also an ancestor
                    return True

            ancestor_nodes[node] = False
            return False

        for root in range(V):
            if not visited_nodes[root]:
                if _is_cyclic(root):
                    return True
        return False
