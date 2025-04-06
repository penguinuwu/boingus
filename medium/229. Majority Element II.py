class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = defaultdict(lambda: 0)
        for n in nums:
            count[n] += 1
        cutoff = len(nums) / 3
        return [n for n, c in count.items() if c > cutoff]
