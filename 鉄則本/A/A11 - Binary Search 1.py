# 入力
n,x = map(int, input().split())
a = list(map(int, input().split()))
# 処理

def search_position(x):
    l = 0
    r = n-1
    while l <= r:
        m = ((l + r) // 2 )
        if x < a[m]:
            r = m - 1
        elif x == a[m]:
            return m + 1
        elif a[m] < x:
            l = m + 1
    return -1

# 出力
print(search_position(x))