"""
1:29:26.65
O(K*E log K*E)
sO(N + K*E)
check solution after 40mins
implemented wrong, tracking price instead of stops 🥀
"""


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = defaultdict(lambda: [])
        for start, end, price in flights:
            adj[start].append((end, price))

        # track stops instead of price to stay within k stops
        stops = { city: math.inf for city in range(n) }
        # but still sort minheap by price
        frontier = [(0, src, 0)]

        while frontier:
            curr_price, curr_city, curr_stops = heapq.heappop(frontier)

            # return after first time city is found
            # because greedy + no negative paths => first is minimum
            if curr_city == dst:
                return curr_price

            # skip, this path reached stop limit
            if curr_stops == k + 1:
                continue

            # skip, another equally stoppy path got here earlier
            if curr_stops >= stops[curr_city]:
                continue
            stops[curr_city] = curr_stops

            # track next stops
            next_stops = curr_stops + 1
            for next_city, next_price in adj[curr_city]:
                if next_stops <= stops[next_city]:
                    heapq.heappush(frontier, (curr_price + next_price, next_city, next_stops))

        return -1
