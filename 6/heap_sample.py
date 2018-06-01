# p30 ヒープの出し入れの実装例

class HeapArray:
    def __init__(self, size):
        self.heap = [0]*size
        self.n = 0

    def push(self, x):
        self.heap[self.n] = x
        child = self.n
        parent = (self.n-1) // 2
        while child != 0 and x < self.heap[parent]:
            self.heap[child] = self.heap[parent]
            child = parent
            parent = (child-1) // 2

        self.heap[child] = x
        self.n += 1

    def pop(self):
        minValue = self.heap[0]
        self.heap[0] = self.heap[self.n-1]
        self.n -= 1
        self.heap[self.n] = 0

        parent = 0
        child = parent*2+1
        while child < self.n:
            if child+1 < self.n and self.heap[child] > self.heap[child+1]:
                child += 1
            if self.heap[parent] <= self.heap[child]:
                break

            t = self.heap[child]
            self.heap[child] = self.heap[parent]
            self.heap[parent] = t

            parent = child
            child = parent*2+1
        return minValue

    def print_h(self):
        print("      ", self.heap[0])
        print("  ", self.heap[1], "       ", self.heap[2])
        print(self.heap[3], "   ", self.heap[4], "   ", self.heap[5], "   ", self.heap[6])

# データを格納してみる
h = HeapArray(7)
h.push(5);
h.print_h();
h.push(6);
h.print_h();
h.push(2);
h.print_h();
h.push(3);
h.print_h();
h.push(1);
h.print_h();
h.pop();
h.print_h();
h.pop();
h.print_h();
