"""
15:40.21
O(n * 2^n)
sO(n)
check answer after 10mins
"""


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        results = []

        def generate_subsets(start_idx, curr_list):
            results.append(curr_list.copy())

            for idx in range(start_idx, n):
                # skip duplicates unless its first encounter
                if idx != start_idx and nums[idx] == nums[idx - 1]:
                    continue

                # add idx
                curr_list.append(nums[idx])
                generate_subsets(idx + 1, curr_list)
                curr_list.pop()

        generate_subsets(0, [])
        return results
