class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_length = math.inf
        curr_sum = 0
        l, r = 0, 0

        while True:
            if curr_sum >= target:
                min_length = min(min_length, r - l)

            if l == r or curr_sum <= target:
                if r >= len(nums):
                    break
                curr_sum += nums[r]
                r += 1

            else:
                curr_sum -= nums[l]
                l += 1

        return 0 if min_length is math.inf else min_length
