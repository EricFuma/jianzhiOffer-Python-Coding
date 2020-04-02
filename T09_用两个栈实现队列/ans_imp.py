class CStack:

    def __init__(self):
        # 栈：   先进后出 --> list 搭配 append(), pop()
        # 队列： 先进先出
        self.queue1 = []
        self.queue2 = []
    def appendHead(self, value: int) -> None:
        queue = self.queue2 if self.queue2 else self.queue1
        queue.append(value)

    def deleteTail(self) -> int:
        # 若队列中没有元素，返回 -1
        if not self.queue1 and not self.queue2:
            return -1
        
        valQueue, tmpQueue = [self.queue1,self.queue2] if self.queue1 else [self.queue2,self.queue1]

        while len(valQueue) > 1:
            tmpQueue.append(valQueue.pop(0))
        return valQueue.pop(0)

myStack = CStack()
myStack.appendHead(1)
myStack.appendHead(2)
myStack.appendHead(3)
myStack.appendHead(4)
myStack.appendHead(5)
myStack.appendHead(6)
print(myStack.deleteTail())
print(myStack.deleteTail())

