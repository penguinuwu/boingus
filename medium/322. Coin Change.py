"""
32:50.46
O(s*n) where s=len(coins), n=amount
sO(n) dp
check solution after 5mins
bottom-up dp but it doesn't feel natural
"""


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coin_count_per_amount = [math.inf] * (amount + 1)
        coin_count_per_amount[0] = 0

        # order of coins don't matter
        for c in coins:
            # try each coin
            for amt in range(c, amount + 1):
                # try to use this coin for every valid amount
                coin_count_per_amount[amt] = min(
                    coin_count_per_amount[amt],
                    coin_count_per_amount[amt - c] + 1,
                )

        return (
            -1
            if coin_count_per_amount[amount] == math.inf
            else coin_count_per_amount[amount]
        )
