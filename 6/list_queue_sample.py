# p18 連結リストでQueue実装

class Node:
    def __init__(self, i, n):
        self.data = i
        self.next = n

class QueueLL:
    def __init__(self):
        self.head = None
        self.tail = None

    def append_q(self, x):
        n = Node(x, None)
        if self.head == None:
            self.head = n
        else:
            self.tail.next = n
        self.tail = n

    def get(self):
        if self.head == None:
            print("overflow")
            return -1

        headValue = self.head.data
        self.head = self.head.next
        return headValue

    def print_q(self):
        n = self.head
        while n != None:
            print(n.data, end=" ")
            n = n.next
        print("head = ", self.head, " tail = ", self.tail)

# データを格納してみる
qu = QueueLL()
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
