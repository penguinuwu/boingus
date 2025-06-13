"""
?
O(mn)
sO(1) no extra data structures created
"""

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])

        def do_not_capture(row, col):
            queue = { (row, col) }
            while queue:
                row, col = queue.pop()
                board[row][col] = "!"
                for drow, dcol in ((0, -1), (0, +1), (-1, 0), (+1, 0)):
                    new_row = row + drow
                    new_col = col + dcol
                    if 0 <= new_row < m and 0 <= new_col < n:
                        if board[new_row][new_col] == "O":
                            queue.add((new_row, new_col))

        # top/bottom row
        for row in (0, m-1):
            for col in range(n):
                if board[row][col] == "O":
                    do_not_capture(row, col)

        # left/right col
        for row in range(m):
            for col in (0, n-1):
                if board[row][col] == "O":
                    do_not_capture(row, col)

        for row in range(m):
            for col in range(n):
                if board[row][col] == "!":
                    board[row][col] = "O"
                elif board[row][col] == "O":
                    board[row][col] = "X"
