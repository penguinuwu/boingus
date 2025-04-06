class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n1, n2, c1, c2 = None, None, 0, 0
        for n in nums:
            if n == n1:
                c1 += 1
            elif n == n2:
                c2 += 1
            elif c1 == 0:
                n1 = n
                c1 = 1
            elif c2 == 0:
                n2 = n
                c2 = 1
            else:
                c1 -= 1
                c2 -= 1

        results = []
        if nums.count(n1) > len(nums) / 3:
            results.append(n1)
        if nums.count(n2) > len(nums) / 3:
            results.append(n2)

        return results
