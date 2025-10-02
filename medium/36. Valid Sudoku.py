"""
22:00.83
O(n^2)
sO(n)
"""


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):

            row_set = set()
            col_set = set()
            sub_set = set()

            for j in range(9):
                row = board[i][j]
                if row in row_set:
                    return False
                if row != ".":
                    row_set.add(row)

                col = board[j][i]
                if col in col_set:
                    return False
                if col != ".":
                    col_set.add(col)

                sub = board[i // 3 * 3 + j // 3][i % 3 * 3 + j % 3]
                if sub in sub_set:
                    return False
                if sub != ".":
                    sub_set.add(sub)

        return True
