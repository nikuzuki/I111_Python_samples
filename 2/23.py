# べき乗の計算

a = 1
for i in range(1, 10000001):    # 1~10,000,000
    a = (a * 293) % 1000
    
print("answer="+str(a))
