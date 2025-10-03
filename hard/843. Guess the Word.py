"""
35:11.94
O(n)
sO(n)
check solution after 7mins
note: try to make connections with any info you get
"""

# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
# class Master:
#     def guess(self, word: str) -> int:


class Solution:
    def findSecretWord(self, words: List[str], master: "Master") -> None:
        def similar_score(str1: str, str2: str) -> int:
            return sum(1 for i in range(6) if str1[i] == str2[i])

        while words:
            # https://leetcode.com/problems/guess-the-word/solutions/556075/how-to-explain-to-interviewer-843-guess-the-word/comments/799347/
            # random increases probability of success allegedly
            curr_word = words.pop(randrange(len(words)))
            master_score = master.guess(curr_word)
            if master_score == 6:
                break

            # https://leetcode.com/problems/guess-the-word/solutions/1318789/careful-explanation-of-two-ideas-that-al-ofs0/
            # observations:
            # 1. if current word scores 0
            # then any word with >0 similar letters CANNOT score 6
            # 2. if current word scores 1
            # then any word with !=1 similar letters CANNOT score 6
            # etc...
            # thus we prune all words where similar_score != master_score

            new_words = []
            for possible_word in words:
                if similar_score(curr_word, possible_word) == master_score:
                    new_words.append(possible_word)
            words = new_words
