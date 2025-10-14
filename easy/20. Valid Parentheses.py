from collections import deque


class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {")": "(", "}": "{", "]": "["}
        stack = deque()
        for c in s:
            if c not in mapping:
                stack.append(c)
            else:
                prev = stack.pop() if stack else None
                if mapping[c] != prev:
                    return False
        return not stack
