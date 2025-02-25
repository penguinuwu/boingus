class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l <= r:
            m = (l + r) // 2

            if target == nums[l]:
                return l
            if target == nums[r]:
                return r
            if target == nums[m]:
                return m

            if (nums[l] < target < nums[m]) or (nums[l] > nums[m] and (nums[l] < target or target < nums[m])):
                # (sorted case) or (pivot within [l, m] and (l < target > m or l > target < m))
                r = m - 1
            elif (nums[m] < target < nums[r]) or (nums[m] > nums[r] and (nums[m] < target or target < nums[r])):
                # (sorted case) or (pivot within [m, r] and (m < target > r or m > target < r))
                l = m + 1
            else:
                return -1

        return -1


"""
[0,1,2,4,5,6,7]
[5,6,7,0,1,2,4]
           1
[4,5,6,7,0,1,2]

[7,0,1,2,4,5,6]
0     _     6  < 7
        4 _ 6  < 7
            6  < 7
-------------
0 _ 2          < 7
    2          < 7
-------------
0              = 7


7,0,1,2,4,5,6
      2        < 3
        4,5,6
          5    > 3
        4
        4

1 2 3 4 5 6 7 8
5 6 7 8 1 2 3 4  <- 3
      8
  6
5
"""
