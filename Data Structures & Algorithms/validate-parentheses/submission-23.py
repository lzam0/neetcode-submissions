class Solution:
    def isValid(self, s: str) -> bool:
        
        closeToOpen = {
         "}": "{",
         "]": "[",
         ")": "("
        }
        
        stack = []

        for bracket in s:
            if bracket in closeToOpen:
                # check if stack is not empty
                # also check if the last value within the stack is a close bracket
                if len(stack) != 0 and stack[-1] == closeToOpen[bracket]:
                    # if its inside then we remove from arr
                    stack.pop(-1)
                else:
                    return False
            # otherwise we append into arr

            else:
                stack.append(bracket)
            print(stack)
        # return true only if valid 
        return len(stack) == 0