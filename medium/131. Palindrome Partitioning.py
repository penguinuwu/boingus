"""
10:41.87
O(n * 2^n)
sO(n)
can be improved with dp but n<=16 so not necessary
"""


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def dfs_partition(start_idx, curr_partition_list):
            if start_idx == n:
                results.append(curr_partition_list.copy())

            for end_idx in range(start_idx, n):
                curr_word = s[start_idx : end_idx + 1]
                if curr_word == curr_word[::-1]:
                    curr_partition_list.append(curr_word)
                    dfs_partition(end_idx + 1, curr_partition_list)
                    curr_partition_list.pop()

        n = len(s)
        results = []
        dfs_partition(0, [])
        return results
