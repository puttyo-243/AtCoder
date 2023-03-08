N = int(input())
A = list(map(int, input().split()))

count_A = {}
for a in A:
    if a not in count_A:
        count_A[a] = 0
    count_A[a] += 1
count_A_list = list(count_A.items())

ans=0
for i in range(len(count_A_list)):
    for j in range(i+1, len(count_A_list)):
        ans += (count_A_list[i][0] - count_A_list[j][0]) ** 2 * count_A_list[i][1] * count_A_list[j][1]

print(ans)