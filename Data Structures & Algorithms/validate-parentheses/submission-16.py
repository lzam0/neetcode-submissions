class Solution:
    def isValid(self, s: str) -> bool:
        closeToOpen = {
            "}": "{",
            ")": "(",
            "]": "["
        }

        stack = []

        for char in s:
            # if it is a closing bracket
            if char in closeToOpen:
                # check if the stack is empty AND if the recent value of the stack is the matching opening bracket
                if stack and stack[-1] == closeToOpen[char]:
                    stack.pop()
                else:
                    # not a matching bracket
                    return False
            else:
                # opening char bracket append it to stack
                stack.append(char)

        # if empty stack true else 
        return True if not stack else False