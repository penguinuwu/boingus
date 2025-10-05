"""
39:43.98
O(n!)
sO(n)
check solution after 27mins
"""


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def place_queens(curr_x, atk_col, atk_diag, atk_adiag, curr_list):
            if len(curr_list) == n:
                return placements.append(curr_list.copy())

            for new_y in range(n):
                diag = curr_x + new_y
                adiag = curr_x - new_y

                if (
                    # dont need atk_row because we recurse (new_x + 1)
                    new_y not in atk_col
                    and diag not in atk_diag
                    and adiag not in atk_adiag
                ):
                    atk_col.add(new_y)
                    atk_diag.add(diag)
                    atk_adiag.add(adiag)
                    curr_list.append((curr_x, new_y))

                    place_queens(curr_x + 1, atk_col, atk_diag, atk_adiag, curr_list)

                    curr_list.pop()
                    atk_adiag.remove(adiag)
                    atk_diag.remove(diag)
                    atk_col.remove(new_y)

        placements = []
        place_queens(0, set(), set(), set(), [])

        boards = []
        for configs in placements:
            b = [["."] * n for _ in range(n)]
            for x, y in configs:
                b[x][y] = "Q"
            boards.append(tuple(str.join("", r) for r in b))
        return boards
