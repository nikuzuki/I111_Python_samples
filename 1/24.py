# forループ - 繰り返し実行
# 1からnまでの2乗和を計算して出力

n = int(input())    # 標準入力で整数値nを代入
ans_sum = 0
for i in range(n+1):    # 0からnまで繰り返し、iでカウントする
    ans_sum = ans_sum + i * i
print(ans_sum)
