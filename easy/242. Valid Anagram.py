"""
3:12.36
O(n)
sO(1) because only 26 letters
i learned about collections.Counter yay
"""

from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)
