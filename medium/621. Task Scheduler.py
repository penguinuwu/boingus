class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = {}
        for task in tasks:
            freq[task] = freq.get(task, 0) + 1

        max_freq = max(freq.values())
        amount_of_max_freqs = tuple(freq.values()).count(max_freq)

        amount_of_partitions = max_freq - 1
        empty_space_per_partition = amount_of_partitions * (n - (amount_of_max_freqs - 1))
        amount_of_tasks_remaining = len(tasks) - (max_freq * amount_of_max_freqs)
        idle = max(0, empty_space_per_partition - amount_of_tasks_remaining)

        return len(tasks) + idle
