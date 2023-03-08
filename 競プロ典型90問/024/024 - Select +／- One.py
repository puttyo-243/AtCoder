input_list = list(map(int,input().split()))
N = input_list[0]
K = input_list[1]

A = list(map(int,input().split()))
B = list(map(int,input().split()))

ab_difference = []
for n in range(N):
    ab_difference.append(abs(A[n] - B[n]))

min = sum(ab_difference)

if min>K:
    print('No')
else:
    if (K-min) % 2 == 0:
        print('Yes')
    else:
        print('No')