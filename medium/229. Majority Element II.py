class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        constraint = 3

        n_c = [[None, 0] for _ in range(constraint - 1)]

        for n in nums:
            for i in range(constraint - 1):
                if n == n_c[i][0]:
                    n_c[i][1] += 1
                    break
            else:
                for i in range(constraint - 1):
                    if n_c[i][1] == 0:
                        n_c[i][0] = n
                        n_c[i][1] = 1
                        break
                else:
                    for i in range(constraint - 1):
                        n_c[i][1] -= 1

        results = []
        for i in range(constraint - 1):
            if nums.count(n_c[i][0]) > len(nums) / constraint:
                results.append(n_c[i][0])

        return results
