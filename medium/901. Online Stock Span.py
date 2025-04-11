"""
11:13.54
O(n) (amortized O(1))
sO(n)
preread solution
"""


class StockSpanner:

    def __init__(self):
        # stack to store the span of each previous max day
        # Monotonic Stack
        self.stack = []

    def next(self, price: int) -> int:
        span = 1

        while self.stack:
            # check previous max price/span
            prev_price, prev_span = self.stack[-1]

            # check if previous max is part of this span
            # if yes, then remove the previous max
            if price >= prev_price:
                span += prev_span
                self.stack.pop()
                # spans requires the days to be consecutive
                # so if next_price < price, it wont get to this prev_price
            else:
                break

        self.stack.append((price, span))
        return span


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
