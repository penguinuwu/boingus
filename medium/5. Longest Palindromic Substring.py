"""
29:45.43
O(n^2)
sO(n^2)
check solution after 1min
dp
"""


class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        res = (0, 0)

        # memo[start][end] => s[start : end+1] is a palindrome
        memo = [[False] * n for _ in range(n)]

        # every letter itself is a palindrome
        for idx in range(n):
            memo[idx][idx] = True

        for check_length in range(1, n):
            for start in range(n - check_length):
                end = start + check_length
                if s[start] == s[end] and (
                    check_length == 1 or memo[start + 1][end - 1]
                ):
                    memo[start][end] = True
                    res = (start, end)

        return s[res[0] : res[1] + 1]
