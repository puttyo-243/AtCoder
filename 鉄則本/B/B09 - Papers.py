## 入力
n = int(input())
a = [0] * n
b = [0] * n
c = [0] * n
d = [0] * n
for i in range(n):
    a[i], b[i], c[i], d[i] = map(int, input().split())


## 処理
z = [[0] * 1501 for _ in range(1501)]

for i in range(n):
    z[b[i]][a[i]] += 1
    z[d[i]][a[i]] -= 1
    z[b[i]][c[i]] -= 1
    z[d[i]][c[i]] += 1

for i in range(0, 1501):
    for j in range(1, 1501):
        z[i][j] = z[i][j-1] + z[i][j]

for i in range(1, 1501):
    for j in range(0, 1501):
        z[i][j] = z[i-1][j] + z[i][j]

ans = 0
for i in range(1501):
    for j in range(1501):
        if z[i][j] > 0:
            ans += 1


## 出力
print(ans)