import bisect

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = sorted(nums, reverse=True)[:k]

    def add(self, val: int) -> int:
        bisect.insort(self.nums, val, key=lambda n: -n)
        if len(self.nums) > self.k:
            self.nums.pop()
        return self.nums[-1]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
