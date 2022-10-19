class MyQueue:

    def __init__(self):
        self.q=[]

    def push(self, x: int) -> None:
        self.q.append(x)

    def pop(self) -> int:
        q2 = []
        for i in range(len(self.q)):
            q2.append(self.q[-1-i])
        self.q=[]
        temp = q2.pop()
        for i in range(len(q2)):
            self.q.append(q2[-1-i])
        return temp

    def peek(self) -> int:
        return self.q[0]

    def empty(self) -> bool:
        return len(self.q)==0



# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
