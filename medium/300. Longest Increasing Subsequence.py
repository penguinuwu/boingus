"""
16:09.88
O(n^2)
sO(n)
preread solution
be careful with duplicates (sequence[prev] **==** nums[curr])
"""


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        sequence = [nums[0]]

        for curr in range(1, len(nums)):
            if nums[curr] > sequence[-1]:
                sequence.append(nums[curr])
            else:
                for prev in range(len(sequence)):
                    # check == because we cannot have duplicates in the sequence
                    if sequence[prev] >= nums[curr]:
                        # note: this sequence will NOT always be valid
                        # but the length will always be the MAX VALID length
                        # because we only append when n > seq[-1]
                        # my explanation sucks but think about it and itll make sense
                        sequence[prev] = nums[curr]
                        break

        return len(sequence)
