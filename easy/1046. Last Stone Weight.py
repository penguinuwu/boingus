import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        h = [-s for s in stones]
        heapq.heapify(h)

        while len(h) > 1:
            s1, s2 = heapq.heappop(h), heapq.heappop(h)
            if s1 != s2:
                heapq.heappush(h, s1 - s2)

        return 0 if len(h) == 0 else -h[0]
