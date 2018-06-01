# 課題5
# Mブロック法

data = [3, 9, 12, 25, 29, 33, 37, 65, 87]

def find(x, n, s):
    m = 3
    k = ((n-1) // m) + 1

    j = 0
    while j <= m-2:
        print((j+1) * k-1, "", end = "")
        if x <= s[(j+1) * k-1]:
            break
        j += 1

    i = j*k
    t = min((j+1)*k-1, n-1)
    while i < t:
        print(i, "")
        if x <= s[i]:
            break
        i += 1

    if x == s[i]:
        return i
    return -1

## targetをdataから探す
target = 87 # 探したい数字
result = find(target, len(data), data)
if result == -1:
    print("not found")
else:
    print("{} is at index {}".format(target, result))

## n=1000として、mを2~20としてm + n/mの値を表示
for i in range(2, 21):
    print(i, i + (1000//i))
