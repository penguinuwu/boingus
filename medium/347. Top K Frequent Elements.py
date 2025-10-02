"""
13:56.73
O(n)
sO(n)
bucket sort lol
"""


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(lambda: 0)
        for n in nums:
            freq[n] += 1

        max_freq = max(freq.values())
        # make max_freq buckets
        buckets = [[] for _ in range(max_freq)]

        for n, count in freq.items():
            buckets[count - 1].append(n)

        # collect k most frequent elements
        result = []
        for i in range(max_freq - 1, -1, -1):
            if len(result) >= k:
                break

            if buckets[i]:
                result.extend(buckets[i])

        return result
