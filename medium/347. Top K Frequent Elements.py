class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = defaultdict(lambda: 0)
        for n in nums:
            counts[n] += 1

		# bucket sort
        buckets = [[] for _ in range(len(nums) + 1)]
        for num, count in counts.items():
            # no need to store a set because
            # It is guaranteed that the answer is unique.
            buckets[count].append(num)

        results = []
        for i in range(len(nums), -1, -1):
            if len(buckets[i]) > 0:
                results.extend(buckets[i])
                if len(results) >= k:
                    break

        return results
