N = int(input())
C = list(map(int,input().split()))

A_all = [x for x in range(1,C[-1]+1)]
A = []
cnt_i = 0
print(A_all)
print(C)
for i in A_all:
    cnt_i += 1
    for j in A_all[cnt_i:]:
        if i < j:
            A.append([i,j])
        else:
            pass
print(A)
print(len(A))