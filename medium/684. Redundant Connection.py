"""
?
O(n) specifically O(n) init * O(a(n)) per operation
sO(n)
preread solution
"""

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parent = list(range(n))
        tree_size = [1] * n


        def find_root(node):
            root = node

            # traverse through parents to find root
            while root != parent[root]:
                root = parent[root]

            # flatten all traversed nodes
            while parent[node] != root:
                node, parent[node] = parent[node], root
                # in case i forgor why:
                # temp = parent[node]
                # parent[node] = root
                # node = temp

            return root


        def union_sets(root1, root2):
            # make root1 is the bigger tree
            # so the traversal flatten is potentially faster
            if tree_size[root2] > tree_size[root1]:
                root1, root2 = root2, root1

            # union roots and record size to root
            parent[root2] = root1
            tree_size[root1] += tree_size[root2]


        for node1, node2 in edges:
            root1 = find_root(node1 - 1)
            root2 = find_root(node2 - 1)

            if root1 == root2:
                return [node1, node2]

            union_sets(root1, root2)

        return []
