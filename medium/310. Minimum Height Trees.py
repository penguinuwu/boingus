"""
38:37.52
O(v+e)
sO(v+e)
check solution after 5mins
leaf trimming is crazy
edit: only enqueue leaf nodes, no need to enqueue everything
"""

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        # centroid can only be 1 (for odd nodes) or 2 (for even nodes)
        if n <= 2:
            return list(range(n))

        # create adjacency list
        edge_map = defaultdict(set)
        for n1, n2 in edges:
            edge_map[n1].add(n2)
            edge_map[n2].add(n1)

        leafs = [node for node in range(n) if len(edge_map[node]) == 1]
        nodes_remaining = n
        while nodes_remaining > 2:
            # delete leafs until only the centroid remains
            # centroid can only be 1 (for odd nodes) or 2 (for even nodes)
            nodes_remaining -= len(leafs)
            new_leafs = []

            for curr_node in leafs:
                # delete its only edge reference
                parent_node = edge_map[curr_node].pop()
                edge_map[parent_node].remove(curr_node)

                # flag whether parent node has become a leaf
                if len(edge_map[parent_node]) == 1:
                    new_leafs.append(parent_node)

            leafs = new_leafs

        return list(leafs)
