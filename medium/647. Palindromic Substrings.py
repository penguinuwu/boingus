"""
9:19.69
O(n^2)
sO(1)
centre 2-pointer expansion
"""


class Solution:
    def countSubstrings(self, s: str) -> int:
        def check(l, r):
            palis = 0
            while 0 <= l and r < n:
                if s[l] == s[r]:
                    palis += 1
                    l -= 1
                    r += 1
                else:
                    break
            return palis

        n = len(s)
        total = 0
        for i in range(n):
            total += check(i, i)
            total += check(i, i + 1)

        return total
