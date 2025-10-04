"""
28:47.42
O(n * 2^n)
sO(n * 2^n)
check solution after 18mins
"""

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        result = []


        def backtrack(start, curr_list) -> None:
            # add itself
            result.append(curr_list[:])

            # iterate through start..n
            for i in range(start, n):
                curr_list.append(nums[i])

                # recurse with i+1..n
                backtrack(i+1, curr_list)

                curr_list.pop()


        backtrack(0, [])
        return result
