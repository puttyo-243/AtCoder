n,x = map(int,input().split())
a_list = list(map(int,input().split()))

ans = 'No'
for i in range(n):
    if x == a_list[i]:
        ans = 'Yes'

print(ans)