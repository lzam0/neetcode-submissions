class Solution:
    def isValid(self, s: str) -> bool:
        closeToOpen = {
            "}": "{",
            ")": "(",
            "]": "["
        }

        stack = []

        # firstly we check if bracket is a closing or not
        for bracket in s:
            # if a bracket is a closing bracket
            if bracket in closeToOpen:
                # then we an pop off the stack
                # ensure that the stack isnt empty already
                # check if the value in the stack is the matching bracket
                if stack and stack[-1] == closeToOpen[bracket]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(bracket)

        # only return true if stack is empty otherwise return false
        return True if not stack else False