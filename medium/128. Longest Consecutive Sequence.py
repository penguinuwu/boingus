class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # https://leetcode.com/problems/longest-consecutive-sequence/solutions/41057/simple-o-n-with-explanation-just-walk-each-streak
        # cool solution but python set in has worst case O(n) ...
        snums = set(nums)
        max_chain = 0

        for n in nums:
            # only walk through streak forwards
            if n - 1 not in snums:
                # the +1 will ensure (curr - n) is at least 1
                curr = n + 1
                while curr in snums:
                    # ... but if we remove curr, then n is decreased lmao
                    snums.remove(curr)
                    curr += 1
                max_chain = max(max_chain, curr - n)

        return max_chain
