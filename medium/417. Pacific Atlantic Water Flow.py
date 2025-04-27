"""
24:26.11
O(mn)
sO(mn)
preread solution
cleaned up
"""


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m = len(heights)
        if m == 0:
            return []
        n = len(heights[0])


        def dfs(to_visit):
            visited = set()
            while to_visit:
                curr_m, curr_n = to_visit.pop()

                visited.add((curr_m, curr_n))

                # add new visits
                curr_height = heights[curr_m][curr_n]
                for dm, dn in ((0, -1), (-1, 0), (0, +1), (+1, 0)):
                    new_m = curr_m + dm
                    new_n = curr_n + dn
                    if 0 <= new_m < m and 0 <= new_n < n and curr_height <= heights[new_m][new_n] and (new_m, new_n) not in visited:
                        to_visit.append((new_m, new_n))

            return visited


        # dfs for pacific/atlantic ocean
        to_visit_p_o = []
        to_visit_a_o = []

        for i in range(m):
            to_visit_p_o.append((i, 0))
            to_visit_a_o.append((m-i-1, n-1))
        for i in range(1, n):
            to_visit_p_o.append((0, i))
            to_visit_a_o.append((m-1, n-i-1))

        to_p_o = dfs(to_visit_p_o)
        to_a_o = dfs(to_visit_a_o)

        return list(to_p_o & to_a_o)
