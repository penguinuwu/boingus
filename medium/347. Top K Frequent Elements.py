"""
7:25.06
O(n log n)
sO(n)
heap sort
"""

import heapq


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(lambda: 0)
        for n in nums:
            freq[n] += 1

        # negate count to work with minheap
        freq_list = [(-count, n) for n, count in freq.items()]
        heapq.heapify(freq_list)

        return [heapq.heappop(freq_list)[1] for _ in range(k)]
