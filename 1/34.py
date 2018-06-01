# 最大値を取得する

# 最大値を求めたいデータが入ったlistを用意
data = [3, 2, 1, 5, 7, 9, 0, 4, 6, 8]
ans_max = data[0]

for i in data:
    if ans_max < i:
        ans_max = i
print("最大値は"+str(ans_max))
