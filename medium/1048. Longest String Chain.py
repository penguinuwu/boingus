"""
42:07.08
O(n^2 L) where L is the max length of a word (16)
sO(nL)
"""

class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        length_to_words = defaultdict(list)
        for w in words:
            length_to_words[len(w)].append(w)

        def is_in_order(pred_word, word):
            skip = 0
            i = 0
            while i < len(pred_word):
                if pred_word[i] == word[i + skip]:
                    i += 1
                elif skip == 0:
                    skip = 1
                else:
                    return False
            return True

        cache = {}
        def dp(word):
            word_length = len(word)
            if word_length == 1:
                return 0

            max_chain = 0

            for pred_word in length_to_words[word_length - 1]:
                if is_in_order(pred_word, word):
                    # pred word found, continue recursion
                    if pred_word not in cache:
                        cache[pred_word] = 1 + dp(pred_word)
                    max_chain = max(max_chain, cache[pred_word])

            return max_chain

        max_word_length = max(length_to_words.keys())
        for i in range(max_word_length, -1, -1):
            for word in length_to_words[i]:
                if word not in cache:
                    cache[word] = 1 + dp(word)

        # print(cache)
        return max(cache.values(), default=0)
