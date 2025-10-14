"""
O(n * 2^(n+n)) -> O(4^n)
sO(n+n) -> sO(n)
note: too much extra space usage
do not make shallow copy if index or append/pop can be used
"""


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []

        def dfs(curr_list, open_b, close_b):
            if open_b == 0 and close_b == 0:
                result.append(curr_list)

            # open
            if open_b > 0:
                dfs(curr_list + ["("], open_b - 1, close_b)

            # close
            if close_b > 0 and close_b > open_b:
                dfs(curr_list + [")"], open_b, close_b - 1)

        dfs([], n, n)
        return [str.join("", l) for l in result]
