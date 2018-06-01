# ミニ演習
# collatz(5)とcollatz(7)の出力は何？

def collatz(n):
    print(n)    # nを出力
    if n == 1:
        return
    elif n % 2 == 0:
        collatz(int(n/2))
    else:
        collatz(3*n+1)

print("---collatz(5)を呼び出す---")
collatz(5)
print("---collatz(5)終了---")
print("---collatz(7)を呼び出す---")
collatz(7)
print("---collatz(7)終了---")
