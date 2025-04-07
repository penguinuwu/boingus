class Solution:
    def decodeString(self, s: str) -> str:
        result = ""
        k = ""
        open_bracket_count = 0
        bracket_start = None

        for i, c in enumerate(s):
            if c == "[":
                open_bracket_count += 1
                if bracket_start is None:
                    bracket_start = i

            elif c == "]":
                open_bracket_count -= 1
                if open_bracket_count == 0:
                    result += int(k) * self.decodeString(s[bracket_start + 1 : i])
                    k = ""
                    bracket_start = None

            elif bracket_start is None:
                if c.isdigit():
                    k += c
                else:
                    result += c

        return result
