"""
O(n)
sO(n)
maintain increasing monotonic stack to track left boundary of each height
and clear out stack of heights when we see a smaller height (right boundary)
"""


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0

        # append a 0 height to flush out remaining heights in stack
        for right_index, h in enumerate(heights + [0]):
            left_index = right_index

            # maintain increasing monotonic stack
            while stack and h < stack[-1][1]:
                left_index, prev_height = stack.pop()
                curr_area = prev_height * (right_index - left_index)
                max_area = max(max_area, curr_area)

            stack.append((left_index, h))

        return max_area
