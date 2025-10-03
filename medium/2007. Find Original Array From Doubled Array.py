"""
17:27.78
O(n)
sO(n)
count sort instead of quicksort
"""


class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        max_changed = max(changed)
        freq = [0] * (max_changed + 1)
        for n in changed:
            freq[n] += 1

        original = []
        n = 0
        while n <= max_changed:
            # all occurrences of n have been accounted for
            if freq[n] == 0:
                n += 1
                continue

            freq[n] -= 1
            original.append(n)

            # check if doubled version exists
            nn = n * 2
            if nn > max_changed or freq[nn] == 0:
                return []
            freq[nn] -= 1

        return original
