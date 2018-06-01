# 2分探索法

def find(x, s):
    print("find {}".format(x))
    left = 0
    right = len(s) - 1
    while True:
        mid = (left + right) // 2
        print(mid)
        print("[{}, {}] mid = {}".format(left, right, mid))
        if x == s[mid]: # 見つかった
            return mid
        if x < s[mid]:  # 左側にあるかも
            right = mid - 1
        else:           # 右側にあるかも
            left = mid + 1
        if left > right:
            break
    return -1

data = [2, 5, 6, 19, 33, 54, 67, 72, 78]

print("result = {}".format(find(75, data)))
print("result = {}".format(find(5, data)))
