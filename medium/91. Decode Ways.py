"""
43:57.77
O(n)
sO(1)
house robber dp
"""


class Solution:
    def numDecodings(self, s: str) -> int:
        zero_to_nine = set(map(str, range(10)))
        zero_to_six = set(map(str, range(7)))
        n = len(s)

        # no way house robber decoder

        # ways to decode s[0]
        # first char must be [1-9]
        prev1 = 0 if s[0] == "0" else 1

        # ways to decode s[0 : 1]
        prev2 = 1

        for i in range(1, len(s)):
            curr = 0

            # first char must be [1-9] again
            if s[i] != "0":
                curr += prev1

            # if first char is 1, second char can be [0-9]
            # if first char is 2, second char can be [0-6]
            prev_i = i - 1
            if (s[prev_i] == "1" and s[i] in zero_to_nine) or (
                s[prev_i] == "2" and s[i] in zero_to_six
            ):
                curr += prev2

            # move to next house lol
            prev2 = prev1
            prev1 = curr

        # house robber
        return prev1
