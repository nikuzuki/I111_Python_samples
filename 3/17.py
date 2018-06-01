# 配列に昇順に要素を入れた場合の探索(改良版)

s = [3, 9, 12, 25, 29, 33, 37, 65, 87]
x = int(input())
print("min : ", s[0])
print("max : ", s[len(s)-1])
sum = 0
for i in s:
    sum += i
print("average : ", sum/len(s))
center = int((len(s)-1)/2)
print("center : ", s[center])
s.append(x+1)   # x+1をsの末尾に追加
i = 0
while(s[i] < x):
    i += 1  # i = i + 1
if s[i] == x:
    print("{}が見つかりました".format(x))
else:
    print("Not Found")
