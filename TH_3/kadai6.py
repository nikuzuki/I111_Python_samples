# 課題6

## A : 素数判定関数を書いた(これは無駄な事が色々ある問題のある関数です)
def check_prime(x):
    # 3からx-1までで割り切れないことを調べれば素数だと分かるという方針
    if x < 2:
        return -1   # 1は素数ではない
    else:
        for i in range(3, x):
            if(x%i==0):  # 途中で割り切れたら素数ではない

                return -1
        return 1    # for文を抜けた == 割り切れなかった == 素数

# Aの関数を使った判定結果
target = 1001
if check_prime(target) == 1:
    print("{}は素数である".format(target))
else:
    print("{}は素数ではない".format(target))

## B : ある数を素因数分解するプログラム(無駄なことを色々してます)
def check_prime_factorization(x):
    ans = ""
    print(str(x)+" = ", end="")
    for i in range(2, x):
        if check_prime(i) == 1:
            while x % i == 0:
                x /= i
                if ans == "":
                    ans += str(i)
                else:
                    ans += " x "
                    ans += str(i)
    print(ans)

# Bの関数の動作確認
check_prime_factorization(24)
check_prime_factorization(360)

## C : Aを用いて1000までの素数を列挙
for i in range(1, 1001):
    if check_prime(i) == 1:
        print(i, end=" ")
print("")
