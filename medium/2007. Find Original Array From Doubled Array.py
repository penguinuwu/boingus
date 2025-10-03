"""
8:15.80
O(n log n)
sO(n)
"""


class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        s_changed = sorted(changed)

        freq = defaultdict(lambda: 0)
        for n in s_changed:
            freq[n] += 1

        original = []
        for n in s_changed:
            # all occurrences of n have been accounted for
            if freq[n] == 0:
                continue

            freq[n] -= 1
            original.append(n)

            nn = n * 2
            # check if doubled version exists
            if freq[nn] == 0:
                return []
            freq[nn] -= 1

        return original
