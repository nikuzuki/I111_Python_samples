kabu = [134, 137, 150, 124, 118, 145,132, 119, 105, 139, 141, 129]
def search_max(kabu, n):
    mxp = 0 # 利益の最大値
    msf = kabu[0] # これまでの最安値
    for j in range(1, n):   # 売るタイミングを固定
        # print("j:"+str(j), "msf:"+str(msf))
        d = kabu[j] - msf
        if d > mxp: # 最大利益を更新
            mxp = d
            print("d", d)
        if kabu[j] < msf:
            msf = kabu[j]
            print(j, "msf", msf)
    return mxp

print(search_max(kabu, len(kabu)))
