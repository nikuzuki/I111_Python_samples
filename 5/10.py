# 一方向連結リストの末尾に新しいレコードを連結するプログラム

# レコードを構成するクラス
class Record:
    next = None
    def __init__(self, value):  # コンストラクタ データを格納
        self.value = value

    def add_next(self, next):   # 次のデータのアドレスを格納
        self.next = next

    def show_value(self):           # 持っているデータを出力
        print(self.value)

    def get_next(self):             # 持っているnextアドレスを返す
        return self.next

# レコードに格納するデータの準備
head = None
data = [1, 2, 3, 4, 5, 6]   # レコードに格納するデータとする

# 先頭だけ作る
head = Record(data[0])
tmp = head  # headが持つアドレスを一時的な変数に渡す
data.pop(0)

# dataを元にレコードを作る
for i in data:
    new_r = Record(i)
    tmp.add_next(new_r)
    tmp = new_r

# できたレコードの内部を先頭から見る
while head != None:
    head.show_value()
    head = head.get_next()
