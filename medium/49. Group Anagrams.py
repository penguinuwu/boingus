class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grams = defaultdict(list)
        for word in strs:
            key = tuple(sorted(list(word)))
            grams[key].append(word)
        return list(grams.values())
