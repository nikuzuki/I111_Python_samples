# ヒープソートを行うプログラム

# ヒープを管理するクラス
class HeapArray:
    # コンストラクタ
    def __init__(self, size):
        self.heap = [0]*size
        self.n = 0

    def push(self, x):
        self.heap[self.n] = x
        child = self.n              # 子供のindex
        parent = (self.n-1) // 2    # 親のindex
        while child != 0 and x < self.heap[parent]:
            self.heap[child] = self.heap[parent]
            child = parent
            parent = (child-1) // 2
        self.heap[child] = x
        self.n += 1

    def pop(self):
        minValue = self.heap[0]
        self.heap[0] = self.heap[self.n-1]    # 末尾を先頭(根)へ
        self.n -= 1
        parent = 0
        child = (parent*2) + 1
        while child < self.n:
            if (child+1) < self.n and self.heap[child] > self.heap[child+1]:
                child += 1
            if self.heap[parent] <= self.heap[child]:
                break
            tmp = self.heap[child]
            self.heap[child] = self.heap[parent]
            self.heap[parent] = tmp
            parent = child
            child = (parent*2) + 1
        return minValue

    def printArray(self):
        print(self.heap)

# Main
data = [65, 12, 46, 97, 56, 33, 75, 53, 21]
print(data)

n = len(data)
heap = HeapArray(n)

for i in range(n):
    heap.push(data[i])

heap.printArray()

for i in range(n):
    print(heap.pop())
