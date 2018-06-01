kabu = [134, 137, 150, 124, 118, 145,132, 119, 105, 139, 141, 129]
def search_max(kabu, n):
    mxp = 0 # 利益の最大値
    for i in range(n-1):
        mxsp = kabu[i]    # 株価の最大値
        for j in range(i+1, n):
            if kabu[j] > mxsp:
                mxsp = kabu[j]
        d = mxsp - kabu[i]
        if d > mxp:
            mxp = d
    return mxp

print(search_max(kabu, len(kabu)))
