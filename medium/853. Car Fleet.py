class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleets = 0
        cap = 0

        for p, s in sorted(zip(position, speed), reverse=True):
            arrival = (target - p) / s
            if arrival > cap:
                fleets += 1
                cap = arrival

        return fleets
