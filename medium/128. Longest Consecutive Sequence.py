"""
6:47.06
O(n)
sO(n)
i forgor check solutions lmao
"""


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        longest = 0

        while nums_set:
            curr = nums_set.pop()

            lower_bound = curr - 1
            while nums_set and lower_bound in nums_set:
                nums_set.remove(lower_bound)
                lower_bound -= 1

            upper_bound = curr + 1
            while nums_set and upper_bound in nums_set:
                nums_set.remove(upper_bound)
                upper_bound += 1

            # note: lower_bound and upper_bound are NOT in array, so need to -1
            longest = max(longest, upper_bound - lower_bound - 1)

        return longest
