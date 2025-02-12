class Solution:
    cache = {}
    mod = 10**9 + 7

    def rearrangeSticks(self, n: int, k: int) -> int:
        if n == 0 or k == 0 or k > n:
            return 0
        if n == 1 or n == k:
            return 1

        cache_key = (n, k)
        if cache_key in self.cache:
            return self.cache[cache_key]

        # fixing sticks right-to-left
        result = 0

        # case: current stick is largest stick
        result += self.rearrangeSticks(n - 1, k - 1)

        # case: current stick is not the largest stick
        result += self.rearrangeSticks(n - 1, k) * (n - 1)

        result %= self.mod

        self.cache[cache_key] = result
        return result

"""
n=1 k=1 => 1

n=3 k=2
=> _ _ 3 => n=2 k=1
    => _ 2 => n=1 k=0
_ _ _

"""
