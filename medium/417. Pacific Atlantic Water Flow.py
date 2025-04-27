"""
24:26.11
O(mn)
sO(mn)
preread solution
"""


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m = len(heights)
        if m == 0:
            return []
        n = len(heights[0])

        def dfs(to_visit, visited):
            while to_visit:
                curr_m, curr_n = to_visit.pop()
                if (curr_m, curr_n) in visited:
                    continue

                visited.add((curr_m, curr_n))

                # add new visits
                curr_height = heights[curr_m][curr_n]
                for dm, dn in ((0, -1), (-1, 0), (0, +1), (+1, 0)):
                    new_m = curr_m + dm
                    new_n = curr_n + dn
                    if 0 <= new_m < m and 0 <= new_n < n and curr_height <= heights[new_m][new_n] and (new_m, new_n) not in visited:
                        to_visit.append((new_m, new_n))

        # dfs for pacific ocean
        to_visit = []
        for i in range(m):
            to_visit.append((i, 0))
        for i in range(n):
            to_visit.append((0, i))
        to_p_o = set()
        dfs(to_visit, to_p_o)

        # dfs for atlantic ocean
        to_visit = []
        for i in range(m):
            to_visit.append((m-i-1, n-1))
        for i in range(n):
            to_visit.append((m-1, n-i-1))
        to_a_o = set()
        dfs(to_visit, to_a_o)

        return list(to_p_o & to_a_o)
