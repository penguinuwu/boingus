class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grams = defaultdict(list)

        for word in strs:
            key = self.hash_str(word)
            grams[key].append(word)

        return list(grams.values())

    def hash_str(self, s: str):
        # strs[i] consists of lowercase English letters
        # so we count the characters
        # thanks neetcode
        counts = [0] * 26

        for c in s:
            counts[ord(c) - ord("a")] += 1

        return tuple(counts)
