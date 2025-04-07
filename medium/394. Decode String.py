class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        curr_str = ""
        k = 0

        for c in s:
            if c == "[":
                stack.append((k, curr_str))
                curr_str = ""
                k = 0

            elif c == "]":
                prev_k, prev_str = stack.pop()
                curr_str = prev_str + (prev_k * curr_str)

            elif c.isdigit():
                k = (k * 10) + int(c)

            else:
                curr_str += c

        return curr_str
