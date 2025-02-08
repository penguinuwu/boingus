class Solution:
    factorials = [1]
    dp = {}
    mod_const = 10**9 + 7

    def __init__(self):
        for i in range(1, 1000):
            self.factorials.append(self.factorials[-1] * i)

    def rearrangeSticks(self, n: int, k: int) -> int:
        if n == k:
            return 1
        if k == 1:
            return self.get_fact(n - 1)
        if n in self.dp and k in self.dp[n]:
            return self.dp[n][k]

        permutations = 0
        permutations_free = self.get_fact(n - 1)
        for first_stick in range(1, n):
            n_visible = n - first_stick
            n_hidden = first_stick - 1

            rearrange_visible = self.rearrangeSticks(n_visible, k - 1)
            permutations_visible = self.get_fact(n_visible)
            # permutations_hidden = self.get_fact(n_hidden)

            # using permutation of multisets equation
            # = (n1 + n2)! / (n1! * n2!)
            # = permutations_free / (permutations_visible * permutations_hidden)
            # then multiply by permutations_hidden * rearrange_visible (like plugging in the multiset)
            # = permutations_free! / (permutations_visible * permutations_hidden) * permutations_hidden * rearrange_visible
            # = permutations_free! / permutations_visible * rearrange_visible
            permutations += ((permutations_free // permutations_visible) * rearrange_visible) % self.mod_const

        # memoize
        if n not in self.dp:
            self.dp[n] = {}
        self.dp[n][k] = permutations

        return permutations % self.mod_const

    def get_fact(self, n):
        if n < len(self.factorials):
            return self.factorials[n]

        # for i in range(len(self.factorials), n + 1):
        #     # f = (self.factorials[-1] * i) % self.mod_const
        #     # self.factorials.append(f)
        #     self.factorials.append(self.factorials[-1] * i)

        # return self.factorials[n]


"""
if n=1 k=1 = 1
1

if n=2 k=1 = (2-1)!
2 1

if n=2 k=2 = 1
1 2

if n=3 k=1 = (3-1)!
3 1 2
3 2 1

if n=3 k=2
1 3 2
-> fix 1 => remain 2 3 => n=2 k=1 rs(n-1, k-1)
2 1 3 / 2 3 1
-> fix 2 => remain 1 3 => n=1 k=1 rs(n-2, k-1)

if n=3 k=3 = 1

if n=4 k=1 = (4-1)!

if n=4 k=2 = 
1 4 2 3 / 1 4 3 2
-> fix 1 => remain 2 3 4 => n=3 k=1 rs(n-1, k-1)
2 1 4 3 / 2 4 1 3 / 2 4 3 1
-> fix 2 => remain 3 4 + 2 => rs(n-2, k-1) ???
3 1 2 4 / 3 1 4 2 / 3 2 1 4 / 3 2 4 1 / 3 4 1 2 / 3 4 2 1
-> fix 3 => remain 4 + 1 2 => n=1 k=1 rs(n-3, k-1) => 1
3! / (2!*1!)
2! = 2

1 2  4 5
x x o o
x o x o
x o o x
o x x o
o x o x
o o x x

4 _ _ _

if 5/5 visible
1 2 3 4 5 visible


"""
