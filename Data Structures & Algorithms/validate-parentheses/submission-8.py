class Solution:
    def isValid(self, s: str) -> bool:
        closeToOpen = {
            '}' : '{',
            ')' : '(',
            ']' : '['
        }

        stack = []
        
        # check if char is in string
        for char in s:
            # check if char is a closing bracket
            if char in closeToOpen:
                # check if stack is NOT empty + check if the top value of the stack is the matching bracket
                if stack and stack[-1] == closeToOpen[char]:
                    stack.pop()
                else:
                    # not a matching bracket
                    return False
            else:
                stack.append(char)

        return True if not stack else False

