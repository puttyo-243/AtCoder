n, q = map(int,input().split())
guests = list(map(int,input().split()))
questions = []
for _ in range(1,q+1):
    questions.append(list(map(int,input().split())))

total_guest = [0] * (n + 1)
for i in range(n):
    if i == 0:
        total_guest[1] = guests[0]
    else:
        total_guest[i+1] = total_guest[i] + guests[i]

for l,r in questions:
    print(total_guest[r] - total_guest[l-1])