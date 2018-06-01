# 課題7

## aのn乗の下二桁を表示する関数
def pow1(a, n):
    ans = 1
    for i in range(n):
        ans *= a
        ans %= 100
    return ans
print(pow1(13, 2))
print(pow1(13, 325))

## 掛け算の回数を減らす
# 2進数を利用する
def pow2(a, n):
    print("a={}, n={}".format(a, n))
    tmp = bin(n)    # 2進数変換
    tmp = tmp[2:]   # 先頭2文字を削除
    tmp2 = tmp
    print(tmp2)
    exp_cnt = 2
    num_cnt = 1     # 1の数を数える
    cnt = 0
    result = [a]
    while len(tmp) != 1:
        if tmp[len(tmp)-1] == "1":
            num_cnt += 1

        if exp_cnt == 2:
            result.append(a*a%100)
            print("a^2 = a x a = {}".format(a*a%100))
            exp_cnt = 4
        else:
            result.append(result[-1]*result[-1]%100)
            print("a^{} = a^{} * a^{} = {}".format(exp_cnt, exp_cnt//2, exp_cnt//2, result[-1]))
            exp_cnt *= 2
        tmp = tmp[:-1] # 末尾を削除
        cnt += 1
    print("{}乗の計算は掛け算{}回で出来る".format(n, cnt+num_cnt-1))


pow2(13, 5)
pow2(13, 325)
