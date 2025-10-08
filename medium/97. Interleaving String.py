"""
13:41.29
O(n1 * n2) n1=len(s1), n2=len(s2)
sO(n1 * n2)
"""


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n1 = len(s1)
        n2 = len(s2)
        n3 = len(s3)

        cache = {}

        def dfs(idx1, idx2, idx3):
            if (idx1, idx2, idx3) in cache:
                return cache[(idx1, idx2, idx3)]

            if idx1 == n1 and idx2 == n2 and idx3 == n3:
                cache[(idx1, idx2, idx3)] = True
                return True

            if idx3 >= n3:
                cache[(idx1, idx2, idx3)] = False
                return False

            interleaving = False

            if idx1 < n1 and s1[idx1] == s3[idx3]:
                interleaving |= dfs(idx1 + 1, idx2, idx3 + 1)

            if idx2 < n2 and s2[idx2] == s3[idx3]:
                interleaving |= dfs(idx1, idx2 + 1, idx3 + 1)

            cache[(idx1, idx2, idx3)] = interleaving
            return interleaving

        return dfs(0, 0, 0)
