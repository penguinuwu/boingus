class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            row_nums = set()
            col_nums = set()
            sub_box_nums = set()
            for j in range(9):
                si = ((i // 3) * 3) + (j // 3)
                sj = ((i % 3) * 3) + (j % 3)

                if (not self.is_unique(board[i][j], row_nums) or \
                    not self.is_unique(board[j][i], col_nums) or \
                    not self.is_unique(board[si][sj], sub_box_nums)):
                    return False

        return True


    def is_unique(self, val, nums_set):
        if val == ".":
            return True

        if val in nums_set:
            return False

        nums_set.add(val)
        return True
