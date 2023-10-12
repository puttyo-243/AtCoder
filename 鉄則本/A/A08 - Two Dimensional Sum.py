h,w = map(int,input().split())
table = []
for _ in range(h):
    table.append(list(map(int,input().split())))
q = int(input())
questions = []
for _ in range(q):
    questions.append(list(map(int,input().split())))


tate = 0
yoko_sum = [[0] * w] * h
tate_sum = [[0] * h] * w
for i in table:
    yoko = 0
    for j in i:
        if yoko == 0:
            yoko_sum[tate][yoko] = j
        else:
            yoko_sum[tate][yoko] = yoko_sum[tate][yoko-1] + j
        yoko += 1
    tate += 1


print(yoko_sum)