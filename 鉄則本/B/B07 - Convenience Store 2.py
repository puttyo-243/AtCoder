t = int(input())
n = int(input())
work_time = []
for _ in range(n):
    work_time.append(list(map(int,input().split())))

workers = [0] * (t+1)
for l,r in work_time:
    workers[l] += 1
    workers[r] -= 1

cnt = 0
ans_list = [0] * (t+1)
for worker in workers:
    if cnt == 0:
        ans_list[cnt] = worker
    else:
        ans_list[cnt] = ans_list[cnt-1] + worker
    cnt += 1

for ans in ans_list[:-1]:
    print(ans)