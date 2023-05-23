N = int(input())
ans = []

for i in range(2**N):
    kakko = []
    for j in range(N):
        if (i >> j) & 1:
            kakko.insert(-j, '(')
        else:
            kakko.insert(-j, ')')
