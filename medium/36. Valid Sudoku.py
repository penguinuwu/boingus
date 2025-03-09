class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            # validate rows n columns
            row_nums = set()
            col_nums = set()
            for j in range(9):
                if not self.is_unique(board[i][j], row_nums) or not self.is_unique(board[j][i], col_nums):
                    return False

        # validate sub-boxes
        for i in range(3):
            for j in range(3):
                sub_box_nums = set()
                for si in range(i*3, i*3 + 3):
                    for sj in range(j*3, j*3 + 3):
                        if not self.is_unique(board[si][sj], sub_box_nums):
                            return False

        return True


    def is_unique(self, val, nums_set):
        if val == ".":
            return True

        if val in nums_set:
            return False

        nums_set.add(val)
        return True
