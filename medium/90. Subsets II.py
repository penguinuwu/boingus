"""
10:22.21
O(n log n * n * n^n) sorting, copying, generating all subsets with 2 recursive calls
sO(n)
dog answer because double recursion and deduplication with set
"""


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        results = set()

        def generate_subsets(start_idx, curr_list):
            if start_idx == n:
                results.add(tuple(sorted(curr_list)))
                return

            for idx in range(start_idx, n):
                # without start_idx
                generate_subsets(idx + 1, curr_list)

                # with start_idx
                curr_list.append(nums[start_idx])
                generate_subsets(idx + 1, curr_list)
                curr_list.pop()

        generate_subsets(0, [])
        return list(results)
