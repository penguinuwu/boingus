"""
O(n)
sO(1)
"""


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1

        while True:  # there exists 1 solution
            total = numbers[left] + numbers[right]
            if total < target:
                left += 1
            elif total > target:
                right -= 1
            else:
                return [left + 1, right + 1]

        # proof:
        # let [a, b, c, ..., x, y, z] be numbers and [b, y] be solution
        # there are 4 ways to miss [b, y]:
        # 1. left=b and right passes y || 2. right=y and left passes b
        # => impossible, left=b right=y == target
        # 3. left passes b while right=z
        # => impossible, if [b+y]==target then [b+z]>target thus right-=1
        # 4. right passes y while left=a
        # => impossible, [a+y]<target thus left+=1
        # therefore this works lmao
