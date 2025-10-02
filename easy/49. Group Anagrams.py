"""
5:50.20
O(n^2 log n)
sO(n)
"""

from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def sort_str(str) -> str:
            return "".join(sorted(str))

        groups = defaultdict(list)

        for word in strs:
            key = sort_str(word)
            groups[key].append(word)

        return list(groups.values())
