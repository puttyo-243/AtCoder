d = int(input())
n = int(input())
date = []
for _ in range(n):
    date.append(list(map(int,input().split())))

li = [0] * (d+1)
for l,r in date:
    li[l-1] += 1
    li[r] -= 1

cnt = 0
ans_list = [0] * (d+1)
for i in li:
    ans_list[cnt] = ans_list[cnt-1] + i
    cnt += 1

for ans in ans_list[:-1]:
    print(ans)