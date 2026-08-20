class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        # create a dict based on the closed to open brackets
        closeToOpen = { ")" : "(", "]" : "[", "}" : "{" }
        
        # iterate through string
        for i in range(len(s)):
            char = s[i]

            # if character is within the dict
            if char in closeToOpen:
                print(stack and stack[-1])
                print(closeToOpen[char])

                # check if the stack isnt empty AND
                # if the top item of the stack the correct opening bracket?
                if stack and stack[-1] == closeToOpen[char]:
                    # remove it off the stack
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)

        return True if not stack else False