class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.items = []
        self.minStack = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.items.append(x)

        if len(self.minStack) > 0:
            self.minStack.append(min(self.minStack[-1], x))
        else:
            self.minStack.append(x)

    def pop(self):
        """
        :rtype: None
        """
        self.items.pop()
        self.minStack.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.items[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.minStack[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()


def main():
    obj = MinStack()
    print(obj)
    obj.push(-3)
    obj.push(2)
    obj.push(4)
    obj.push(1)
    obj.pop()
    param_3 = obj.top()
    param_4 = obj.getMin()
    print(param_3, param_4)


if __name__ == "__main__":
    main()
