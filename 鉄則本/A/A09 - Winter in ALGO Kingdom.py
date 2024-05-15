## 入力
h, w, n = map(int,input().split())

a = [0] * n
b = [0] * n
c = [0] * n
d = [0] * n
for i in range(n):
    a[i], b[i], c[i], d[i] = map(int, input().split())


## 処理
z = [[0] * (w+2) for i in range(h+2)]
for i in range(n):
    z[a[i]][b[i]] += 1
    z[a[i]][d[i]+1] -= 1
    z[c[i]+1][b[i]] -= 1
    z[c[i]+1][d[i]+1] += 1

for i in range(1, h+1):
    for j in range(1, w+1):
        z[i][j] = z[i][j-1] + z[i][j]

for i in range(1, h+1):
    for j in range(1, w+1):
        z[i][j] = z[i-1][j] + z[i][j]


## 出力
for i in range(1, h+1):
    for j in range(1,w+1):
        if j < w:
            print(z[i][j], end=' ')
        if j == w:
            print(z[i][j], end='\n')