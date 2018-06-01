# 課題2
# 昇順逐次探索法をベースに書いた

## find関数
def find(x, s):
    s.append(x+1)   # dataの末尾にtarget+1を追加
    i = 0
    while s[i] < x:
        i += 1
    if x == s[i]:
        return i
    else:
        return -1

data = [3, 9, 12, 25, 29, 33, 37, 65, 87]

# targetをdataから探す
target = 17
result = find(target, data)
if result == -1:
    print("not found")
else:
    print("{} is at index {}".format(target, i))

## 平均値を求める
print("average is {}".format(sum(data)/len(data)))

## 最大値/最小値を求める
print("maximum data is {} at address {}".format(data[0], 0))
print("minimum data is {} at address {}".format(data[len(data)-2], len(data)-2))

## 中央値
data.pop(len(data)-1)
print(data)
if (len(data))%2==1:  # データ数が奇数の時(末尾が一つ増えているので注意)
    print("Midian is {}".format(data[len(data)//2]))
else:
    print(data[len(data)//2], data[(len(data)//2)-1])
    print("Midian is {}".format((data[len(data)//2]+data[(len(data)//2)-1])/2))
