"""
O(n)
sO(n)
decreasing monotonic stack !!!!!!
"""


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        prev_temps = []
        for i, v in enumerate(temperatures):
            while prev_temps and v > prev_temps[-1][0]:
                _prev_v, prev_i = prev_temps.pop()
                res[prev_i] = i - prev_i
            prev_temps.append((v, i))
        return res
