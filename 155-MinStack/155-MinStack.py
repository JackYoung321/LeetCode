class MinStack:

    def __init__(self):
        self.elements = []
        self.minElement = []
    def push(self, val: int) -> None:
        self.elements.append(val)
        
        val = min(val, self.minElement[-1] if self.minElement else val) #New method learned with if statement embedded in                                                                       parameters. Min function returns lower               
                                                                     #of two parameters, returns last value of minElement
                                                                    #stack if self.minElement isn't empty otherwise insert
                                                                    #the first value to it.
        self.minElement.append(val)

    def pop(self) -> None:
        self.elements.pop()
        self.minElement.pop()

    def top(self) -> int:
        return self.elements[-1]

    def getMin(self) -> int:
        return self.minElement[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
