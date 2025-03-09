class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)

        for s in strs:
            h = self.str_to_hash(s)
            anagrams[h].append(s)

        return list(anagrams.values())


    def str_to_hash(self, s):
        # strs[i] consists of lowercase English letters
        # so we count the characters
        # thanks neetcode
        count_chars = [0] * 26

        for c in s:
            count_index = ord(c) - ord("a")
            count_chars[count_index] += 1

        return tuple(count_chars)
