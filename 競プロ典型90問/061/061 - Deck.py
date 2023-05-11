Q = int(input())
work = []
for i in range(Q):
    work_n = list(map(int,input().split()))
    work.append(work_n)

deck = []
ans_list = []
for w in work:
    t = w[0]
    x = w[1]
    if t == 1:
        deck.insert(0,x)
    if t == 2:
        deck.append(x)
    if t == 3:
        ans_list.append(deck[x - 1])

for ans in ans_list:
    print(ans)