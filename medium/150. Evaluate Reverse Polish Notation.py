class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        while tokens:
            curr = tokens.pop(0)

            # this is "pythonic" hehe
            try:
                stack.append(int(curr))
            except ValueError:
                self.evaluate(stack, curr)

        return stack[0]
    
    def evaluate(self, stack: List[int], operation: str):
        n2 = int(stack.pop())
        n1 = int(stack.pop())

        if operation == "+":
            stack.append(n1 + n2)
        elif operation == "-":
            stack.append(n1 - n2)
        elif operation == "*":
            stack.append(n1 * n2)
        elif operation == "/":
            stack.append(math.trunc(n1 / n2))
        else:
            raise RuntimeError()
