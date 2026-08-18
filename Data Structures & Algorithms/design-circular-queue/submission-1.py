class Node:
    def __init__(self, prev=None, nxt=None, value=None):
        self.prev = prev
        self.nxt = nxt
        self.val = value

class MyCircularQueue:

    def __init__(self, k: int):
        # Init queue with size k
        self.head = Node()
        temp = self.head
        for i in range(k-1):
            temp.nxt = Node(temp, None, None)
            temp = temp.nxt
        temp.nxt = self.head
        self.head.prev = temp
        self.end = self.head

    def enQueue(self, value: int) -> bool:
        # Insert item into circular queue, true if successful
        if self.isEmpty():
            self.head.val = value
            self.end = self.head
            return True
        elif not self.isFull():
            self.end.nxt.val = value
            self.end = self.end.nxt
            return True
        else:
            return False

    def deQueue(self) -> bool:
        # Delete item fron queue, true is successful
        if self.isEmpty(): return False
        self.head.val = None
        self.head = self.head.nxt
        return True

    def Front(self) -> int:
        # Return front item of queue or -1
        return self.head.val if not self.isEmpty() else -1

    def Rear(self) -> int:
        # Return last item of queue or -1
        return self.end.val if not self.isEmpty() else -1

    def isEmpty(self) -> bool:
        return True if self.head.val == None else False

    def isFull(self) -> bool:
        return True if self.head.prev.val != None else False


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()