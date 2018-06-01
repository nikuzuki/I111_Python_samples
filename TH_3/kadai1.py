# 課題1
# 逐次探索法をベースに書いた

## 関数find
def find(target, data):
    for i in data:
        if i == target:
            return i
    return -1

data = [37, 12, 25, 9, 87, 33, 65, 3, 29]   # データが偶数個
# data = [37, 12, 25, 99, 9, 87, 33, 65, 3, 29] # データが奇数個

## targetをdataから探す
target = 87 # 探したい数字
result = find(target, data)
if result == -1:
    print("not found")
else:
    print("{} is at index {}".format(target, result))

## 平均値を求める
print("average is {}".format(sum(data)/len(data)))

## 最大値/最小値を求める max(data)は使わない
max_value = data[0]
min_value = data[0]
max_index = 0
min_index = 0
for (i, d) in enumerate(data):  # dataの番地をiに、dataの中身をdに入れて回す
    if max_value < d:
        max_value = d
        max_index = i
    if min_value > d:
        min_value = d
        min_index = i
print("maximum data is {} at address {}".format(max_value, max_index))
print("minimum data is {} at address {}".format(min_value, min_index))

## 中央値を考える
# バブルソートで昇順に並べる
for i in range(len(data)-1, 0 , -1):
    for j in range(i):
        if data[j] > data[j+1]:
            tmp = data[j+1]
            data[j+1] = data[j]
            data[j] = tmp
print(data)
if len(data)%2==1:  # データ数が奇数の時
    print("Midian is {}".format(data[len(data)//2]))
else:
    print("Midian is {}".format(data[len(data)//2]+data[(len(data)//2)-1]/2))
