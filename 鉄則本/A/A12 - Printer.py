## 入力
n, k = map(int, input().split())
a_list = list(map(int, input().split()))

## 処理
def check(x):
    sum = 0
    for i in range(n):
        sum += x // a_list[i]
    if sum >= k:
        return True
    else:
        return False

def main():
    l = 1
    r = 1000000000
    while l < r:
        m = (l + r) // 2
        ans = check(m)
        if ans == True:
            r = m
        else:
            l = m + 1

    return l

## 出力
print(main())