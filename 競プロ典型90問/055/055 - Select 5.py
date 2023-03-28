from itertools import combinations

N, P, Q = map(int,input().split())
A_in = list(map(int,input().split()))

if P == 0:
    print(0)
    exit()

comb = combinations(A_in,5)

ans = 0
for a, b, c, d, e in comb:
    if a % P * b % P * c % P * d % P * e % P == Q:
        ans += 1

print(ans)