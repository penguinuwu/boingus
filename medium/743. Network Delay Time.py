"""
1:13:00.00
O(E log E) or O(E log V) == O(2E log V) == O(E log V^2) because V=E^2
sO(E + V)
i forgor dihstra
"""

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # make adj list
        adjacency = defaultdict(lambda: {})
        for start, end, dist in times:
            adjacency[start-1][end-1] = dist

        # compute distances from k
        distances = { node: math.inf for node in range(n) }
        frontier = [(0, k-1)]

        while frontier:
            curr_dist, curr_node = heapq.heappop(frontier)

            # already visited -> skip
            if curr_dist >= distances[curr_node]:
                continue
            distances[curr_node] = curr_dist

            # first visit on this path -> check neighbours
            for next_node, next_dist in adjacency[curr_node].items():
                dist = curr_dist + next_dist
                if dist < distances[next_node]:
                    heapq.heappush(frontier, (dist, next_node))

        max_distance = max(distances.values())
        return -1 if max_distance == math.inf else max_distance
