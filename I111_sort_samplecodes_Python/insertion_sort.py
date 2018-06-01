# 挿入法でソートを行うプログラム

data = [65, 12, 46, 97, 56, 33, 75, 53, 21]
n = len(data)
print(data)
for i in range(1, n):
    x = data[i]
    j = i
    while data[j-1]>x and j>0:  # 末尾から先頭までxより大きいものを右へずらす
        data[j] = data[j-1]
        j -= 1
    data[j] = x
print(data)
