"""
9:32.00
O(n log n)
sO(n)
think carefully
"""


class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        nums_with_index = [(n, i) for i, n in enumerate(nums)]
        nums_with_index.sort(reverse=True)

        top_k = nums_with_index[:k]
        top_k.sort(key=lambda x: x[1])

        answer = [n for n, _ in top_k]
        return answer
