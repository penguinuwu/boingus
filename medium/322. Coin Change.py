"""
17:52.26
O(s*n) without dp O(s^n) where s=len(coins), n=amount
sO(n) dp
check solution after 5mins
top-down dp + "dfs" + "backtrack"
"""


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = {}

        def dfs_backtrack_dp(curr_amount):
            if curr_amount in dp:
                return dp[curr_amount]

            if curr_amount < 0:
                dp[curr_amount] = math.inf
                return dp[curr_amount]

            if curr_amount == 0:
                dp[curr_amount] = 0
                return dp[curr_amount]

            min_coins_needed = math.inf

            for c in coins:
                curr_coins_needed = dfs_backtrack_dp(curr_amount - c)
                min_coins_needed = min(min_coins_needed, curr_coins_needed + 1)

            dp[curr_amount] = min_coins_needed
            return dp[curr_amount]

        coins_needed = dfs_backtrack_dp(amount)
        return -1 if coins_needed is math.inf else coins_needed
