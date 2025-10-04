"""
48:57.68
O(n * 2^n)
sO(n * 2^n)
check solution after 18mins
really clean recursive solution
https://leetcode.com/problems/subsets/editorial/comments/1265962/?parent=449948
"""


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return [[]]

        subsets = self.subsets(nums[:-1])
        new = [ss + [nums[-1]] for ss in subsets]

        return subsets + new
