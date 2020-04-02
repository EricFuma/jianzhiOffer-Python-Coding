class CQueue:
    
    def __init__(self):
        # 栈：   先进后出 --> list 搭配 append(), pop()
        # 队列： 先进先出
        self.storeStack = []
        self.helpStack = []
    
    # 方法2：544ms
    
    # 元素入队
    def appendTail(self, value: int) -> None:
        self.storeStack.append(value)
    
    # 元素出队
    def deleteHead(self) -> int:
        # 若队列中没有元素，返回 -1
        if not self.helpStack:
            if not self.storeStack:
                return -1
            else:
                while self.storeStack:
                    self.helpStack.append(self.storeStack.pop())  
        val = self.helpStack.pop() 
        return val
      
    
    
    # 方法1：请务必忘了它，2140ms
    '''
    def deleteHead(self) -> int:
        # 若队列中没有元素，返回 -1
        if not self.storeStack:
            return -1
        while self.storeStack:
            self.helpStack.append(self.storeStack.pop())
        val = self.helpStack.pop()
        while self.helpStack:
            self.storeStack.append(self.helpStack.pop())
        return val
    '''
      


# Your CQueue object will be instantiated and called as such:
# obj = CQueue()
# obj.appendTail(value)
# param_2 = obj.deleteHead()
