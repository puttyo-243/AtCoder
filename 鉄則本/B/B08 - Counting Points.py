n = int(input())
x = [0] * n
y = [0] * n
for i in range(n):
    x[i], y[i] = map(int,input().split())

q = int(input())
a = [0] * q
b = [0] * q
c = [0] * q
d = [0] * q
for i in range(q):
    a[i], b[i], c[i], d[i] = map(int,input().split())

z = [[0] * (max(x)+1) for i in range(max(y)+1)]


for i in range(n):
    z[y[i]][x[i]] += 1

for i in range(1,len(z)):
    for j in range(1,len(z[0])):
        z[i][j] = z[i-1][j] + z[i][j]

for i in range(1,len(z)):
    for j in range(1,len(z[0])):
        z[i][j] = z[i][j-1] + z[i][j]


for i in range(q):
    print(z[d[i]][c[i]] - z[d[i]][a[i]-1] - z[b[i]-1][c[i]] + z[b[i]-1][a[i]-1])