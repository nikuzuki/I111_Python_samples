# p16 配列でQueue実装
class Queue:

    def __init__(self, maxsize):
        self.queue = [0]*maxsize
        self.head = 0
        self.tail = 0

    def append_q(self, x):
        self.tail = (self.tail + 1) % len(self.queue)
        self.queue[self.tail] = x
        if self.tail == self.head:
            print("this queue is full.")

    def get(self):
        if self.tail == self.head:
            print("this queue is empty.")
            return -1

        self.head = (self.head + 1) % len(self.queue)
        t = self.queue[self.head]
        self.queue[self.head] = 0
        return t

    def print_q(self):
        print(self.queue)
        print("h:", self.head, " t", self.tail)

# データを格納してみる
qu = Queue(3)
qu.append_q(3)
qu.print_q()
qu.append_q(4)
qu.print_q()
print("get=", qu.get())
qu.print_q()
qu.append_q(5)
qu.print_q()
print("get=", qu.get())
qu.append_q(6)
qu.print_q()
