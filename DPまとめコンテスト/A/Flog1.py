N = int(input())
h_list = list(map(int,input().split()))

def flog_jump():

    memo = [float('inf')] * N
    memo[0] = 0
    for i in range(1,N):
        if i == 1:
            memo[i] = abs(h_list[i] - h_list[i-1])
        else:
            memo[i] = min(
                memo[i-1] + abs(h_list[i] - h_list[i-1]),
                memo[i-2] + abs(h_list[i] - h_list[i-2])
                )
    
    return memo[N-1]

print(flog_jump())