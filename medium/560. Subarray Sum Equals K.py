class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sums = defaultdict(lambda: 0)
        sums[0] = 1

        count = 0
        curr_sum = 0

        for n in nums:
            curr_sum += n

            target = curr_sum - k
            count += sums[target]

            # must be appended after the count increment
            # order is important
            # e.g. nums=[1] k=0
            sums[curr_sum] += 1

        return count
