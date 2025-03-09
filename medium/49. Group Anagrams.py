class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)

        for s in strs:
            h = self.str_to_hash(s)
            anagrams[h].append(s)

        return list(anagrams.values())


    def str_to_hash(self, s):
        return str.join("", sorted(s))
