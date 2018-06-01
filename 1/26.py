# forループ - 繰り返し実行
# 1からnまでの(2i-1)^2を計算して出力

n = int(input())    # 標準入力で整数値nを代入
ans_sum = 0
for i in range(1, n+1):    # 0からnまで繰り返し、iでカウントする
    ans_sum = ans_sum + (2*i-1) * (2*i-1)
print(ans_sum)
