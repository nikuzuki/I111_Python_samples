# バブルソートを行うプログラム

data = [65, 12, 46, 97, 56, 33, 75, 53, 21]
print(data)
n = len(data)
for k in range(1, n):
    for i in range(n-k):
        if data[i] > data[i+1]: # 右側に大きいデータがある時入れ替え
            tmp = data[i]
            data[i] = data[i+1]
            data[i+1] = tmp
print(data)
