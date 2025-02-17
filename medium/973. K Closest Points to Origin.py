import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dist = lambda x1, x2: sqrt(x1 ** 2 + x2 ** 2)
        dists = [(dist(*p), p) for p in points]
        results = heapq.nsmallest(k, dists, key=lambda d: d[0])
        return [p for _, p in results]
