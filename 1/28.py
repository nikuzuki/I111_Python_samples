# ユークリッドの互除法
a = int(input())
b = int(input())

# Pythonにはdo-whileが無いのでwhileで代用
while True:
    r = a % b
    a = b
    b = r
    if r == 0:
        break
print("G.C.D.="+str(a))
