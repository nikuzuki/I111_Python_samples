# 逐次探索法(番兵付き)
# 入力 任意の実数
# 出力 s[i]==xとなるiがあればiを出力

s = [37, 12, 25, 9, 87, 33, 65, 3, 29]
i = 0;

x = int(input())
n = len(s)  # nはsの長さとする
s.append(x) # sの末尾にxを追加

while x != s[i]:
    i += 1  # i = i + 1

if i < n:
    print("{}は{}番目にありました".format(x, i))
else:
    print("Not found")
