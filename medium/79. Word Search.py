"""
23:31.13
O(m * n * 3^w) mn=len(entire board), w=len(word), 4 directions but no going back so 3 directions
sO(w)
"""


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def find_word(curr_word, curr_x, curr_y, visited):
            if curr_word == word:
                return True

            curr_n = len(curr_word)
            if curr_n == word_n:
                return False

            # curr_n is the length, so indexing by it automatically does +1
            target_char = word[curr_n]
            for dx, dy in ((1, 0), (0, 1), (-1, 0), (0, -1)):
                new_x = curr_x + dx
                new_y = curr_y + dy
                new_pair = (new_x, new_y)

                # check OOB
                if new_x < 0 or new_x >= m or new_y < 0 or new_y >= n:
                    continue

                # check if char is wrong or has been visited
                if board[new_x][new_y] != target_char or new_pair in visited:
                    continue

                # potential path found
                visited.add(new_pair)
                if find_word(curr_word + target_char, new_x, new_y, visited):
                    return True

                # not found, backtrack
                visited.remove(new_pair)

            return False

        word_n = len(word)
        m = len(board)
        n = len(board[0])

        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    visited = set()
                    visited.add((i, j))
                    if find_word(word[0], i, j, visited):
                        return True

        return False
