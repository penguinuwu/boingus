class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for c in tokens:
            if c == "+":
                stack.append(stack.pop() + stack.pop())
            elif c == "*":
                stack.append(stack.pop() * stack.pop())
            elif c == "-":
                temp = stack.pop()
                stack.append(stack.pop() - temp)
            elif c == "/":
                temp = stack.pop()
                stack.append(math.trunc(stack.pop() / temp))
            else:
                stack.append(int(c))

        return stack[-1]
