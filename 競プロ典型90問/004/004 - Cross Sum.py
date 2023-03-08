H,W = map(int,input().split())
A=[]
for _ in range(H):
    A.append(list(map(int,input().split())))

row = []
for a in A:
    row.append(sum(a))

A_ = [list(x) for x in zip(*A)]

column = []
for a_ in A_:
    column.append(sum(a_))

for i in range(H):
    ans = []
    for j in range(W):
        ans.append(row[i] + column[j] - A[i][j])
    print(*ans)
'''cnt = 0
for a in A:
    ans = list(map(lambda x:(sum(x) + sum(A[cnt]) - x[cnt]), A_))
    print(*ans)
    cnt += 1
'''

    