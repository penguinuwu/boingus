"""
29:53.45
O(v+e)
sO(v+e)
check solution after 5mins
leaf trimming is crazy
"""

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        tree = defaultdict(set)

        # link nodes together by edges
        for n1, n2 in edges:
            tree[n1].add(n2)
            tree[n2].add(n1)

        nodes = set(range(n))
        while len(nodes) > 2:
            # delete leafs until only the centroid remains
            # centroid can only be 1 (for odd nodes) or 2 (for even nodes)

            # mark leafs for deletion later
            # we cannot delete in 1 iteration because that might delete non-leafs
            leafs = []
            for curr_node in nodes:
                if len(tree[curr_node]) == 1:
                    # leaf found, mark for deletion
                    leafs.append(curr_node)

            for curr_node in leafs:
                # delete its only edge reference
                parent_node = tree[curr_node].pop()
                tree[parent_node].remove(curr_node)
                nodes.remove(curr_node)

        return list(nodes)
