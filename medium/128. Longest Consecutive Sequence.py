class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # https://leetcode.com/problems/longest-consecutive-sequence/solutions/41055/my-really-simple-java-o-n-solution-accepted/comments/191109/

        snums = set(nums)
        max_chain = 0

        for n in nums:
            if n not in snums:
                continue

            left = n - 1
            while left in snums:
                snums.remove(left)
                left -= 1

            right = n + 1
            while right in snums:
                snums.remove(right)
                right += 1

            # n-1 and n+1 introduced an extra +2
            # we need to keep +1 because number itself is consecutive 1
            # so we do -1 to get rid of extra +1
            max_chain = max(max_chain, right - left - 1)

            if len(snums) == 0:
                break

        return max_chain
