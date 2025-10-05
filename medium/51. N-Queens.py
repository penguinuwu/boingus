"""
33:14.66
O(n^3 * n!) because extra triple loop each recursion
sO(n)
check solution after 27mins and found a typo lmao
really funny implementation
"""


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def can_attack(q1, q2):
            return (
                q1[0] == q2[0]
                or q1[1] == q2[1]
                # check diagonal
                or q1[0] + q1[1] == q2[0] + q2[1]
                # check anti-diagonal
                or q1[0] - q1[1] == q2[0] - q2[1]
            )

        def place_queens(curr_x, curr_list):
            if len(curr_list) == n:
                return placements.append(curr_list.copy())

            for new_x in range(curr_x, n):
                for new_y in range(n):
                    new_pair = (new_x, new_y)
                    for prev_pair in curr_list:
                        if can_attack(new_pair, prev_pair):
                            break
                    else:
                        curr_list.append(new_pair)
                        place_queens(new_x + 1, curr_list)
                        curr_list.pop()

        placements = []
        place_queens(0, [])

        boards = []
        for configs in placements:
            b = [["."] * n for _ in range(n)]
            for x, y in configs:
                b[x][y] = "Q"
            boards.append(tuple(str.join("", r) for r in b))
        return boards
