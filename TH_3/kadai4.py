# 課題4
# 課題1で使用したバブルソートを利用する
data = [37, 12, 25, 9, 87, 33, 65, 3, 29]

# バブルソートを行う関数
def bubble_sort(data):
    # バブルソートで昇順に並べる
    for i in range(len(data)-1, 0 , -1):
        for j in range(i):
            if data[j] > data[j+1]:
                tmp = data[j+1]
                data[j+1] = data[j]
                data[j] = tmp
    return data

print(data)
print(bubble_sort(data))
