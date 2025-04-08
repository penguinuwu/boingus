class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        results = [0] * n
        hottest = temperatures[-1]

        for curr_i in range(n-2, -1, -1):
            if temperatures[curr_i] >= hottest:
                hottest = temperatures[curr_i]
                continue

            next_i = curr_i + 1
            while next_i < n:
                if temperatures[curr_i] < temperatures[next_i]:
                    results[curr_i] = next_i - curr_i
                    break
                elif temperatures[curr_i] < temperatures[next_i + results[next_i]]:
                    results[curr_i] = next_i + results[next_i] - curr_i
                    break
                else:
                    next_i += 1

        return results
