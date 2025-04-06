class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # every value *before* this index == 0
        i0 = 0
        # every value *before* this index == 1
        i1 = 0
        # every value *after* this index == 2
        i2 = len(nums) - 1

        # loop from value == 0/1 until value == 2
        while not i1 > i2:
            if nums[i1] == 2:
                nums[i1], nums[i2] = nums[i2], nums[i1]
                i2 -= 1
            elif nums[i1] == 0:
                nums[i1], nums[i0] = nums[i0], nums[i1]
                i0 += 1
                i1 += 1
            else:
                i1 += 1
