class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for val in tokens:
            print(val)

            if val == "+":
                # get the last 2 values of the stack
                add = stack[-1] + stack[-2]
                stack.pop()
                stack.pop()
                stack.append(add)
            elif val == "*":
                multi = stack[-1] * stack[-2]
                stack.pop()
                stack.pop()
                stack.append(multi)
            elif val == "/":
                div = int(stack[-2] / stack[-1])
                stack.pop()
                stack.pop()
                stack.append(div)
            elif val == "-":
                sub = stack[-2] - stack[-1]
                stack.pop()
                stack.pop()
                stack.append(sub)
            else:
                stack.append(int(val))
        return stack[-1]

        