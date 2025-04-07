class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n
        count = 0

        i_start = 0
        while count < n:
            i_curr = i_start
            temp = nums[i_curr]

            while True:
                i_next = (i_curr + k) % n
                i_curr = i_next
                nums[i_curr], temp = temp, nums[i_curr]

                count += 1

                if i_curr == i_start:
                    break

            i_start += 1

"""
[1,2,3,4,5,6,7], k = 3
[_,2,3,1,5,6,7] 4
[1,2,3,1,5,6,4] 7
[5,6,7,1,2,3,4]
"""
