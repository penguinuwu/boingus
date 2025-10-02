"""
2:42.25
O(n)
sO(n)
"""


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letters = defaultdict(lambda: 0)

        for c in s:
            letters[c] += 1
        for c in t:
            letters[c] -= 1

        for counts in letters.values():
            if counts != 0:
                return False
        return True
