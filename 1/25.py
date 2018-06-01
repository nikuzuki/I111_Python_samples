# forループ - 繰り返し実行
# (2i - 1)^2のiが1~nの時の総和を計算

n = int(input())    # 標準入力で整数値nを代入
ans_sum = 0
for i in range(1, 2*n, 2):  # 1から~2*nまで繰り返す、iは2ずつ増える
    ans_sum = ans_sum + i * i
print(ans_sum)
