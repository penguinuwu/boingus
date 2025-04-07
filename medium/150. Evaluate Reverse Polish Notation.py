class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops = set(("+", "-", "*", "/"))
        stack = []

        for curr in tokens:
            if curr in ops:
                self.evaluate(stack, curr)
            else:
                stack.append(int(curr))

        return stack[0]
    
    def evaluate(self, stack: List[int], operation: str):
        n2 = stack.pop()
        n1 = stack.pop()

        if operation == "+":
            stack.append(n1 + n2)
        elif operation == "-":
            stack.append(n1 - n2)
        elif operation == "*":
            stack.append(n1 * n2)
        elif operation == "/":
            stack.append(int(n1 / n2))
        else:
            raise RuntimeError()
