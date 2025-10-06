"""
26:55.38
O(n log n)
sO(n)
preread solution
be careful with duplicates (sequence[prev] **==** nums[curr])
dp with binary search that took like 10mins to debug
"""


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        sequence = [nums[0]]

        for curr in range(1, len(nums)):
            if nums[curr] > sequence[-1]:
                sequence.append(nums[curr])
            else:
                l = 0
                r = len(sequence) - 1
                while l < r:
                    m = (l + r) // 2
                    if nums[curr] < sequence[m]:
                        r = m
                    elif nums[curr] > sequence[m]:
                        l = m + 1
                    else:
                        l = r = m
                sequence[l] = nums[curr]

        return len(sequence)
