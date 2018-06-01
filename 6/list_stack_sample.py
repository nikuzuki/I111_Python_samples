# p8 連結リストを使ったstackの実装

class Node:

    def __init__(self, i, n):
        self.data = i
        self.next = n


class StackLL:

    def __init__(self):
        self.top = None

    def push(self, x):
        n = Node(x, self.top)
        self.top = n

    def pop(self):
        if self.top != None:
            topvalue = self.top.data
            self.top = self.top.next
            return topvalue
        else:
             print("overflow(Negative)")

    def print_stack(self):
        n = self.top
        while n != None:
            print(n.data, end=" ")
            n = n.next
        print("top=>", self.top)

# stackを作る
st = StackLL()
st.push(3)
st.print_stack()
st.push(4)
st.print_stack()
st.push(5)
st.print_stack()
print("pop=", st.pop())
st.print_stack()
