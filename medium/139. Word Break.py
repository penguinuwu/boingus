"""
7:17.71
O(n^3) where n=len(s), dp has n states, each state creates n substrings, and each substring is hashed
sO(n)
"""


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        word_dict = set(wordDict)

        @cache
        def dp(start_idx):
            if start_idx == n:
                return True

            curr_word = ""
            for curr_idx in range(start_idx, n):
                curr_word += s[curr_idx]
                if curr_word in word_dict and dp(curr_idx + 1):
                    return True
            return False

        return dp(0)
