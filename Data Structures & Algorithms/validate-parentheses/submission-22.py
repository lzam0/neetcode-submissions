class Solution:
    def isValid(self, s: str) -> bool:
        closeToOpen = {
            "}": "{",
            "]": "[",
            ")": "("
        }

        stack = []

        for char in s:
            # check if the char is a closing bracket
            if char in closeToOpen:
                # check if stack is empty OR top doesnt match
                if len(stack) == 0 or stack[-1] != closeToOpen[char]:
                    return False    
                # remove the most recent opening
                stack.pop()
            else:
                # otherwise add it to the top of the stack
                stack.append(char)
            print(char)

        # return true if s is a valid string - eg if stack is empty
        return len(stack) == 0


        # example 1: s = []
        # is [ a closing bracket? -> no then we add it to the stack
        # is ] a closing bracket -> yes then we pop the first
        # output: check if stack is empty -> true

        # example 2: s = ([{}])

        # is ( a closing bracket -> no add it to stack | stack = (
        # is [ a closing bracket -> no add it to stack | stack = ([
        # is { a closing bracket -> no add it to stack | stack = ([{
        # is } a closing bracket -> yes, check if the top of the stack is the opening bracket and remove it