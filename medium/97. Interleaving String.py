"""
22:15.59
O(n1 * n2) n1=len(s1), n2=len(s2)
sO(n1 * n2)
clean up 2d memoization
"""


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n1 = len(s1)
        n2 = len(s2)
        n3 = len(s3)

        if n1 + n2 != n3:
            return False
        if s1 == s3 or s2 == s3:
            return True

        cache = [[None] * (n2 + 1) for _ in range(n1 + 1)]

        def dfs(idx1, idx2, idx3):
            if not cache[idx1][idx2] is None:
                return cache[idx1][idx2]

            if idx1 == n1 and idx2 == n2 and idx3 == n3:
                cache[idx1][idx2] = True
                return True

            if idx3 >= n3:
                cache[idx1][idx2] = False
                return False

            cache[idx1][idx2] = False

            if idx1 < n1 and s1[idx1] == s3[idx3]:
                cache[idx1][idx2] |= dfs(idx1 + 1, idx2, idx3 + 1)

            if idx2 < n2 and s2[idx2] == s3[idx3]:
                cache[idx1][idx2] |= dfs(idx1, idx2 + 1, idx3 + 1)

            return cache[idx1][idx2]

        return dfs(0, 0, 0)
