# mブロック法
import math
s = [3, 9, 12, 25, 29, 33, 37, 65, 87]

j = 0
n = len(s)  # sの長さ
x = int(input())
m = 3   # sを3等分するとする
k = math.ceil(n/m)  # 切り上げ

# どのブロックを探すか決める
while j <= m-2:
    if x <= s[(j+1)*k-1]:
        break
    else:
        j += 1

# 決めたブロック内を探索する
i = j * k
t = min((j+1)*k-1, n-1)
while i < t:
    if x <= s[i]:
        break
    else:
        i += 1
if x == s[i]:
    print("見つかりました")
else:
    print("NotFound")
