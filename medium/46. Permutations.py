"""
11:55.42
O(n * n!) because nPn = n!/(n-n)! = n! and copy of curr_list is O(n)
sO(n)
check solution after 2mins
"""


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        result = []

        def generate_permutes(curr_list, curr_set):
            # all numbers used
            if len(curr_list) == n:
                result.append(curr_list.copy())
                return

            for num in nums:
                # use a set to keep track of used numbers
                if num not in curr_set:
                    curr_set.add(num)
                    curr_list.append(num)

                    generate_permutes(curr_list, curr_set)

                    curr_list.pop()
                    curr_set.remove(num)

        generate_permutes([], set())
        return result
