# 2進数展開のプログラム
bit = []
n = int(input())
k = 0
while True:
    bit.append(n%2)
    n = int(n/2)
    print("bit[{}]={} n={}".format(k, bit[k], n))
    k += 1
    if n <= 0:
        break
print("出力結果 : ", end="")
for i in (reversed(bit)):
    print(i, end="")
print("")
