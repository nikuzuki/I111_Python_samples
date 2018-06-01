# シェルソートを行うプログラム

data = [65, 12, 46, 97, 56, 33, 75, 53, 21]
print(data)
n = len(data)

gap = n // 2
while gap > 0:
    i = gap
    while i < n:
        j = i - gap
        while j >= 0 and data[j] > data[j+gap]:
            tmp = data[j]
            data[j] = data[j+gap]
            data[j+gap] = tmp
            j -= gap
        i += 1
    gap = gap // 2
    print(data)
