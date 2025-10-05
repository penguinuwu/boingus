"""
35:23.37
O(n^2)
sO(1)
check solution after 1min
centre expansion
"""


class Solution:
    def longestPalindrome(self, s: str) -> str:
        def find_palindrome(start, end):
            nonlocal res

            while 0 <= start and end < n:
                if s[start] != s[end]:
                    break

                if (end - start) > (res[1] - res[0]):
                    res = (start, end)

                start -= 1
                end += 1

        n = len(s)
        res = (0, 0)
        for centre in range(n):
            find_palindrome(centre, centre)
            find_palindrome(centre, centre + 1)

        return s[res[0] : res[1] + 1]
