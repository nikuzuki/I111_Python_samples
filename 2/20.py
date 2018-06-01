# べき乗の計算

a = 1
for i in range(1, 10000001):    # 1~10,000,000
    a *= 293
b = a % 1000    # 下三桁
print("answer="+str(b))
