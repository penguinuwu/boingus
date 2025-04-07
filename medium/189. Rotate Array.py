class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n

        # this is so crazy
        self.reverse(nums, 0, n - 1)
        self.reverse(nums, 0, k - 1)
        self.reverse(nums, k, n - 1)

    def reverse(self, nums: List[int], s: int, e: int) -> None:
        """
        less memory than [::-1]
        """
        while s < e:
            nums[s], nums[e] = nums[e], nums[s]
            s += 1
            e -= 1
