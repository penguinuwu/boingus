"""
22:40.94
O(v+e)
sO(v) worst case store all vertices in frontier
check solution after 8mins
mistake: be careful with variable names 💀
"""

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return None

        # initialize node clone map with start node
        node_to_clone = {node: Node(val=node.val, neighbors=[])}
        to_visit = deque((node,))

        while to_visit:
            curr_node = to_visit.popleft()

            # create clones of neighbours (referenced in clone map)
            # then append to current node clone
            for next_node in curr_node.neighbors:

                # check if node has been visited
                if next_node not in node_to_clone:
                    # create clone and attach to clone map
                    node_to_clone[next_node] = Node(val=next_node.val, neighbors=[])
                    to_visit.append(next_node)

                # update clone neighbours
                node_to_clone[curr_node].neighbors.append(node_to_clone[next_node])

        return node_to_clone[node]
