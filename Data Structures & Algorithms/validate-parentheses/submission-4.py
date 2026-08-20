class Solution:
    def isValid(self, s: str) -> bool:
        closeToOpen = {
            ')' : '(',
            '}' : '{',
            ']' : '['
        }
        
        # empty stack
        stack = []

        # firstly we iterate through the arr
        for i in range(len(s)):
            curr = s[i]

            # check if curr value is inside of the arr
            if curr in closeToOpen:
                print(stack)
                # check if stack is empty
                # does the opening bracket at the top stack match the closing bracket im currently looking at
                if stack and stack[-1] == closeToOpen[curr]:
                    stack.pop()
                else:

                    return False
            else:
                # if it isnt then append to arr
                stack.append(curr)


        # shall return false if there are values in stack
        # shall return true if values are not in stack
        return len(stack) == 0
        