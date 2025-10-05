"""
32:51.14
O(2^n)
sO(n) not counting output array, only counting recursion depth, which is like DFS
check solution after 11mins for deduplication
"""


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates_s = sorted(candidates)
        n = len(candidates_s)
        results = []

        def generate_combinations(start_idx, curr_sum, curr_list):
            if curr_sum > target:
                return
            if curr_sum == target:
                results.append(curr_list.copy())

            for idx in range(start_idx, n):
                # remove duplicates
                # BUT Note how duplicates are allowed when start_idx==idx
                # this is so duplicates are allowed 1 TIME ONLY !!
                # each duplicate is allowed for the first iteration of the recursive call
                if start_idx < idx and candidates_s[idx] == candidates_s[idx - 1]:
                    continue

                # small speedup hack by breaking early because list is sorted
                new_sum = curr_sum + candidates_s[idx]
                if new_sum > target:
                    break

                curr_list.append(candidates_s[idx])
                generate_combinations(idx + 1, new_sum, curr_list)
                curr_list.pop()

        generate_combinations(0, 0, [])
        return results
