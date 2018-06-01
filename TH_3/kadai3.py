# 課題3
# 0番地の数字を足しても昇順を保つ関数を作る

data = [3, 9, 12, 25, 29, 33, 37, 65, 87]

def arrangement(data, x):
    data[0] += x
    for i in range(len(data)-1):
        if data[i] > data[i+1]:
            tmp = data[i]
            data[i] = data[i+1]
            data[i+1] = tmp
    return data

print(arrangement(data, 40))
