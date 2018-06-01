# 逐次探索法
# 入力 任意の実数
# 出力 s[i]==xとなるiがあればiを出力

s = [37, 12, 25, 9, 87, 33, 65, 3, 29]
x = int(input())
for i in range(len(s)): # sの長さ分、iを回す
    if x == s[i]:
        print("{}は見つかりました".format(x))
        break
