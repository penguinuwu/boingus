"""
8:37.35
O(nk) where n = len(words), k = max len(word)
sO(nk)
"""

from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def hash_str(word) -> Tuple[int]:
            # 26 because "strs[i] consists of lowercase English letters"
            key = [0] * 26
            for c in word:
                key[ord(c) - ord("a")] += 1
            return tuple(key)

        groups = defaultdict(list)

        for word in strs:
            key = hash_str(word)
            groups[key].append(word)

        return list(groups.values())
