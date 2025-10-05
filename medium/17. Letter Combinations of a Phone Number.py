"""
7:36.53
O(n * 4^n)
sO(n)
"""

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mapping = {
            "2": ("a", "b", "c",),
            "3": ("d", "e", "f",),
            "4": ("g", "h", "i",),
            "5": ("j", "k", "l",),
            "6": ("m", "n", "o",),
            "7": ("p", "q", "r", "s",),
            "8": ("t", "u", "v",),
            "9": ("w", "x", "y", "z",),
        }

        n = len(digits)
        results = []

        if n == 0:
            return results

        def backtrack(start_idx, curr_list):
            if start_idx == n:
                results.append(str.join("", curr_list))
                return
            for c in mapping[digits[start_idx]]:
                curr_list.append(c)
                backtrack(start_idx + 1, curr_list)
                curr_list.pop()

        backtrack(0, [])
        return results
 