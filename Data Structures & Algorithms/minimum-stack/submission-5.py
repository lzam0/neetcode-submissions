class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []
        self.mini = 0

    def push(self, val: int) -> None:
        # print("before push",self.minStack, self.stack)
        self.stack.append(val)

        # check if the stack is empty
        if len(self.minStack) == 0:
            # append it to the minStack
            self.minStack.append(val)
        else:
            # compare between val and the most recent value within stack
            self.minStack.append(min(val, self.minStack[-1]))
        # print(self.minStack, self.stack)

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]