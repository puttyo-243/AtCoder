n = list(map(int,list(input())))
n.reverse()

ans = 0
for i in range(len(n)):
    ans += n[i] * (2 ** i)
print(ans)