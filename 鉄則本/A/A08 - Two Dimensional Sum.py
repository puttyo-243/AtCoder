h,w = map(int,input().split())
x = [None] * h
z = [[0] * (w+1) for i in range(h+1)]
for i in range(h):
    x[i] = list(map(int,input().split()))

q = int(input())
a = [None] * q
b = [None] * q
c = [None] * q
d = [None] * q
for i in range(q):
    a[i],b[i],c[i],d[i] = map(int,input().split())

for i in range(1,h+1):
    for j in range(1,w+1):
        z[i][j] = z[i][j-1] + x[i-1][j-1]

for i in range(1,w+1):
    for j in range(1,h+1):
        z[i][j] = z[i-1][j] + z[i][j]

for i in range(q):
    print(z[c[i]][d[i]] - z[a[i]-1][d[i]] - z[c[i]][b[i]-1] + z[a[i]-1][b[i]-1])