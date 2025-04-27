"""
38:04.12
O(4 * (d + 10^4)) where d==deadends and 4==wheels and 10==wheel_range
sO(4 * (d + 10^4))

analysis:
- init target -> 4 wheels => O(4)
- init deadends -> 4 wheels => O(4 * d)
- try every permutation
-> 10^4 (numbers^wheels) permutations
-> 2 operations (-1, +1) per wheel
=> O(2*4 * 10^4) => O(4 * 10^4)

add together: O(4 * (d + 10^4))

mistake: starting position can be in deadends
mistake: misread question as move can be +/-[1, 9]
"""


class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        target = tuple(int(c) for c in target)
        deadends = set((tuple(int(c) for c in s) for s in deadends))

        visited = set()
        queue = []

        start_seq = (0, 0, 0, 0)
        if start_seq not in deadends:
            queue.append((start_seq, 0))

        while queue:
            curr_seq, curr_moves = queue.pop(0)

            if curr_seq == target:
                return curr_moves

            for w in range(4): # 4 wheels
                curr_seq_list = list(curr_seq)

				# # misread question as rotate a wheel any amount
                # for new_value in range(10): # rotate between 0-9
                #     curr_seq_list[w] = new_value
                #     new_seq = tuple(curr_seq_list)

                for m in (-1, +1): # rotate move
                    new_value = curr_seq[w] + m

                    # if-else is faster than mod for hardcoded range
                    if new_value < 0:
                        curr_seq_list[w] = 9
                    elif new_value > 9:
                        curr_seq_list[w] = 0
                    else:
                        curr_seq_list[w] = new_value

                    new_seq = tuple(curr_seq_list)
                    if new_seq not in visited and new_seq not in deadends:
                        visited.add(new_seq)
                        queue.append((new_seq, curr_moves + 1))

        return -1
