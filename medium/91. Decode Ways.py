"""
18:53.59
O(n) without memo O(2^n)
sO(n) recursive stack
top-down dp + "dfs" + "backtrack"
"""


class Solution:
    def numDecodings(self, s: str) -> int:
        zero_to_nine = set(map(str, range(10)))
        zero_to_six = set(map(str, range(7)))
        n = len(s)

        @cache
        def dfs_backtrack(start_idx):
            # reached the end
            if start_idx == n:
                return 1

            # first char must be [1-9]
            if s[start_idx] == "0":
                return 0
            total = dfs_backtrack(start_idx + 1)

            # if first char is 1, second char can be [0-9]
            # if first char is 2, second char can be [0-6]
            next_idx = start_idx + 1
            if next_idx < n:
                if (s[start_idx] == "1" and s[next_idx] in zero_to_nine) or (
                    s[start_idx] == "2" and s[next_idx] in zero_to_six
                ):
                    total += dfs_backtrack(next_idx + 1)

            return total

        return dfs_backtrack(0)
