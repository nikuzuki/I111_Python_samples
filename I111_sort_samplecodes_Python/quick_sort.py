# クイックソートを行うプログラム

data = [65, 12, 46, 97, 56, 33, 75, 53, 21]

def qsort(a, left, right):
    if right <= left:
        return
    i = left
    j = right
    x = a[(i+j) // 2]

    while i <= j:
        while a[i] < x:
            i += 1
        while a[j] > x:
            j -= 1
        if i <= j:  # 入れ替え
            t = a[i]
            a[i] = a[j]
            a[j] = t
            i += 1
            j -= 1

    qsort(a, left, j)
    qsort(a, i, right)

print(data)

n = len(data)
qsort(data, 0, n-1)
print(data)
