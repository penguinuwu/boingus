"""
6:35.14
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
            curr_longest = 1

            lower_bound = curr - 1
            while nums_set and lower_bound in nums_set:
                nums_set.remove(lower_bound)
                curr_longest += 1
                lower_bound -= 1

            upper_bound = curr + 1
            while nums_set and upper_bound in nums_set:
                nums_set.remove(upper_bound)
                curr_longest += 1
                upper_bound += 1

            longest = max(curr_longest, longest)

        return longest
