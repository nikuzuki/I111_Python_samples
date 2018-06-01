# p7の配列を使ったスタック例
class Stack:

    def __init__(self, maxsize):
        self.data = [0]*maxsize
        self.top = 0

    def push(self, x):
        if self.top < len(self.data):
            self.data[self.top] = x
            self.top += 1
        else:
            print("overflow")

    def pop(self):
        if self.top > 0:
            self.top -= 1
            return self.data[self.top]
        else:
            print("overflow(Negative)")
            return -1

    def print_stack(self):
        print(self.data)
        print(self.top)

# サイズ6のスタックを作る
st = Stack(6)
st.push(3)
st.print_stack()
st.push(4)
st.print_stack()
st.push(5)
st.print_stack()
print("pop=", st.pop())
st.print_stack()
