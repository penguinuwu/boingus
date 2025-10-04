"""
12:28.23
O(n ^ ((t/m) + 1)) n=len(candidates), t=target, m=min(candidates)
sO(t/m) or sO(t) only counting recursion depth, not counting output array
max number of nodes in n-ary tree of height d is (n^(d+1) - 1) / (n-1) = O(n^(d+1))
took like an hour to figure out the time complexity lol
attempt at backtracking from memory 💀👍
"""


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        results = set()
        n = len(candidates)

        def backtrack(curr_list, start_idx, total):
            if total == target:
                results.add(tuple(curr_list))
                return

            if total > target:
                return

            for idx in range(start_idx, n):
                curr_list.append(candidates[idx])
                backtrack(curr_list, idx, total + candidates[idx])
                curr_list.pop()

        backtrack([], 0, 0)
        return list(results)
