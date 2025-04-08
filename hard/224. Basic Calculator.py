class Solution:
    def __init__(self):
        # shared index for recursive iteration
        # https://leetcode.com/problems/basic-calculator/editorial/comments/386603/
        self.shared_index = 0

        self.operations = {
            "-": lambda a, b: a - b,
            "+": lambda a, b: a + b,
            None: lambda _, b: b,
        }

    def calculate(self, s: str) -> int:
        term = 0
        prev_operation = None
        result = 0

        while self.shared_index < len(s):
            curr = s[self.shared_index]
            self.shared_index += 1

            if curr == " ":
                continue

            elif curr.isdigit():
                term = term * 10 + int(curr)

            elif curr == "(":
                # recurse on brackets !!!
                term = self.calculate(s)

            elif curr == ")":
                break

            else:
                # compute current operation to result
                result = self.operations[prev_operation](result, term)

                # clear current term and load new operation
                term = 0
                prev_operation = curr

        # in case of close-bracket or end-of-str
        # finish up the previous operation
        return self.operations[prev_operation](result, term)
