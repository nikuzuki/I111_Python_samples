# 閏年判定例

year = int(input())
if year%400==0 or (year%100!=0 and year%4==0):
    print(str(year)+"年は閏年です.")
else:
    print(str(year)+"年は閏年ではありません.")
