class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        # print("before push",self.minStack, self.stack)
        self.stack.append(val)

        # check if the stack is empty
        if len(self.minStack) == 0:
            # append it to the minStack
            self.minStack.append(val)
        else:
            # compare between val and the most recent value within stack
            # append the smallest value to stack
            self.minStack.append(min(val, self.minStack[-1]))
        # print(self.minStack, self.stack)

    def pop(self) -> None:
        # remove the most recent value of stack
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        # return the top value of stack
        return self.stack[-1]

    def getMin(self) -> int:
        # minimum value is the most recent value in stack
        return self.minStack[-1]