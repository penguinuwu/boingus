"""
O(n)
sO(n)
dp solution
"""


class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left_max = [0]
        for h in height:
            left_max.append(max(left_max[-1], h))

        volume = 0
        right_max = 0
        for i in range(n - 1, 0, -1):
            min_wall = min(left_max[i + 1], right_max)
            volume += max(0, min_wall - height[i])
            right_max = max(right_max, height[i])

        return volume
