class Solution:
    def getSum(self, a: int, b: int) -> int:
        # constraint is -1000 so its within 2^10, need 10 bit mask?
        mask = 0b1111111111

        while (b & mask) != 0:
            carry = (a & b) << 1
            a = a ^ b
            b = carry

        if b != 0:
            return a & mask
        else:
            return a
