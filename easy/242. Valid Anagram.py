"""
3:12.36
O(n)
sO(n)
i learned about collections.Counter yay
"""

from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)
