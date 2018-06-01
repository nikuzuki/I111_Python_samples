# ハッシュ法の動くプログラム

m = 10
htb = [0]*10    # 0が10個入ったlistを作る

def hash(x):
    return x % m

def add(x):
    j = hash(x)
    while htb[j] != 0:
        j = (j+1) % m
    htb[j] = x

def find(x):
    j = hash(x)
    while htb[j] != 0:
        if htb[j] == x: # 見つかった時
            return j
        j = (j+1) % m
    return -1

# ハッシュテーブルにデータを入れる
add(3)
add(23)
add(4)
add(19)
add(9)

# ハッシュテーブルの中身を確認する
print(htb)

# 検索してみる
print("4 is at {}".format(find(4)))
print("29 is at {}".format(find(29)))
