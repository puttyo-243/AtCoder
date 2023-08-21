N = int(input())
A,B,C = map(int,input().split())

ans = 10000
for x in range(10000):
    for y in range(10000):
        value = x*A + y*B
        if value > N or (N - value) % C != 0:
            continue
        
        z = (N - value) // C
        if ans > x + y + z:
            ans = x + y + z

print(ans)