"""
32:28.51
O(n * m) n=len(coins), m=amount
sO(n * m)
check solution after 20mins
"""


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        cache = {}

        def dfs(start_idx, rem):
            if (start_idx, rem) in cache:
                return cache[(start_idx, rem)]

            if rem == 0:
                cache[(start_idx, rem)] = 1
                return 1

            if start_idx >= len(coins) or rem < 0:
                return 0

            cache[(start_idx, rem)] = dfs(start_idx + 1, rem)
            if coins[start_idx] <= amount:
                cache[(start_idx, rem)] += dfs(start_idx, rem - coins[start_idx])

            return cache[(start_idx, rem)]

        # DOnt do this again
        # O(n * m * m) because of the while loop
        # e.g. coins=[1,2], amount=100
        # dfs(0, 100): while loop makes 101 calls to dfs(1, x)
        # dfs(1, 100): while loop makes 51 calls to dfs(2, x)
        # dfs(1, 99): while loop makes 50 calls to dfs(2, x)
        # ...
        # Even though it's all cached, the number of calls is still O(n * m * m)

        # ways = 0
        # new_rem = rem
        # while new_rem >= 0:
        #     way = dfs(start_idx + 1, new_rem)
        #     cache[(start_idx + 1, new_rem)] = way
        #     ways += way
        #     new_rem -= coins[start_idx]

        # cache[(start_idx, rem)] = ways
        # return ways

        return dfs(0, amount)
