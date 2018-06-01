# 10.pyを元に、データの挿入/削除を行う

# レコードを構成するクラス
class Record:
    next = None
    def __init__(self, value):  # コンストラクタ データを格納
        self.value = value

    def add_next(self, next):   # 次のデータのアドレスを格納
        self.next = next

    def show_value(self):           # 持っているデータを出力
        print(self.value, end = " ")

    def get_next(self):             # 持っているnextアドレスを返す
        return self.next

## データの挿入を行う関数
def add_Record(num, data, head):  # 引数(num番地に挿入、挿入するdata, head)
    new_r = Record(data)
    cnt = 0
    p = head
    while p != None:
        if num == cnt:    # 先頭に入れる場合
            # headが持つ次のデータのアドレスを新しく作ったデータのnextに入れる
            new_r.add_next(p)
            if num == 0:
                head = new_r
                return head
            else:
                p_after.add_next(new_r)
                return head
        p_after = p
        p = p.get_next()
        cnt += 1

    # 最後まで行った場合は末尾に追加
    p_after.add_next(new_r)
    return head

## データの削除を行う関数
def delete_Record(num, head):   # 引数(削除する番地、head)
    cnt = 0
    p = head
    while p != None:
        if cnt == num:
            if cnt == 0:
                head = p.get_next()
            else:
                p.value = p.next.value
                p.next = p.next.next
            return head
        p = p.get_next()
        cnt += 1

## レコード全体を出力する関数
def show_Records(head):
    print("レコード全体を確認")
    p = head
    while p != None:
        p.show_value()
        p = p.get_next()
    print("")

# main レコードに格納するデータの準備
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

# できたレコードの全体を先頭から見る
show_Records(head)

# データの5番地に29を挿入
head = add_Record(5, 29, head)

# 挿入できているか確認
show_Records(head)

# データの0番地を削除
head = delete_Record(1, head)

# 削除できているか確認
show_Records(head)
