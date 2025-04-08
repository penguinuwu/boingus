class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        results = [0] * len(temperatures)
        prev_temps = []

        for curr_i, curr_temp in enumerate(temperatures):
            while prev_temps and prev_temps[-1][1] < curr_temp:
                prev_i = prev_temps.pop()[0]
                results[prev_i] = curr_i - prev_i

            prev_temps.append((curr_i, curr_temp))

        return results
