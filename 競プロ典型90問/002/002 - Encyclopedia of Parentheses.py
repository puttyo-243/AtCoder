N = int(input())

li = ['('] * (N//2) + [')'] * (N//2)
for i in range(2**N):
    parentheses = []
    for j in range(N):
        if (i >> j) & 1:
            parentheses.append(li[j])
    
    #条件判定
    ans = []
    
    
    print(''.join(ans))

