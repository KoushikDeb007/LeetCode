class MyCircularDeque:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the deque to be k.
        """
        self.cap = k
        self.front, self.rear = -1, -1
        self.arr = [-1] * self.cap
        self.n = 0

    def insertFront(self, value: int) -> bool:
        """
        Adds an item at the front of Deque. Return true if the operation is successful.
        """
        if self.n != self.cap:
            if self.n == 0:
                self.front, self.rear = 0, 0
            self.arr.insert(self.front, value)
            self.n += 1
            return True
        return False

    def insertLast(self, value: int) -> bool:
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
        """
        if self.n != self.cap:
            if self.n == 0:
                self.front, self.rear = 0, 0
            else:
                self.rear = (self.rear + 1) % self.cap
            self.arr.insert(self.n, value)
            self.n += 1
            return True
        return False

    def deleteFront(self) -> bool:
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        """
        if not self.isEmpty():
            self.arr.pop(0)
            self.n -= 1
            return True
        return False

    def deleteLast(self) -> bool:
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        """
        if not self.isEmpty():
            self.arr.pop(self.n - 1)
            self.n -= 1
            return True
        return False

    def getFront(self) -> int:
        """
        Get the front item from the deque.
        """
        return self.arr[0] if self.front != -1 else -1

    def getRear(self) -> int:
        """
        Get the last item from the deque.
        """

        return self.arr[self.n - 1] if self.rear != -1 else -1

    def isEmpty(self) -> bool:
        """
        Checks whether the circular deque is empty or not.
        """
        return self.n == 0

    def isFull(self) -> bool:
        """
        Checks whether the circular deque is full or not.
        """
        return self.n == self.cap

# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()