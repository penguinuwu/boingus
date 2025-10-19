"""
O(n)
sO(1)
2 pointers solution
works because we guarantee to only calculate volume when local min wall is found
"""


class Solution:
    def trap(self, height: List[int]) -> int:
        volume = 0

        left = 0
        max_left = 0
        right = len(height) - 1
        max_right = 0

        while left < right:
            # left is min wall
            if height[left] <= height[right]:
                if max_left <= height[left]:
                    max_left = height[left]
                else:
                    curr_volume = max_left - height[left]
                    volume += curr_volume
                left += 1

            # can we move both left and right at the same time?

            # right is min wall
            if left < right and height[left] >= height[right]:
                if max_right <= height[right]:
                    max_right = height[right]
                else:
                    curr_volume = max_right - height[right]
                    volume += curr_volume
                right -= 1

        return volume
