"""
O(n log n)
sO(n)
yay
"""


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        position_speed = sorted(zip(position, speed), reverse=True)
        fleets = 0
        min_speed_fleet = -math.inf

        for p, s in position_speed:
            eta = (target - p) / s

            if eta > min_speed_fleet:
                min_speed_fleet = eta
                fleets += 1

        return fleets


"""
0 1 2 3 4 5 6 7 8 9101112
                    x   x 1
                x         x 1
          x x x x x x x x 7
      x     x     x     x 3
x                         12

                x   | 1
            x     x | 2
"""
