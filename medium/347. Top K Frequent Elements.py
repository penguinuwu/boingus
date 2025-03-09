import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = defaultdict(lambda: 0)
        for n in nums:
            counts[n] += 1

        order = [(-count, num) for num, count in counts.items()]
        heapq.heapify(order)

        return [heapq.heappop(order)[1] for _ in range(k)]
