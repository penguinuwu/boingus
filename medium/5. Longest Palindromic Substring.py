"""
10:30.24
O(n^3)
sO(1)
check solution after 1min
brute force
"""


class Solution:
    def longestPalindrome(self, s: str) -> str:
        def check(start, end):
            while start < end:
                if s[start] != s[end]:
                    return False
                start += 1
                end -= 1
            return True

        res = (0, 0)
        for i in range(len(s)):
            for j in range(i, len(s)):
                if (j - i) > (res[1] - res[0]) and check(i, j):
                    res = (i, j)
        return s[res[0] : res[1] + 1]
