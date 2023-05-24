import sys
N = int(sys.stdin.readline())

ans = []

for i in range(2**N):
    kakko = [0] * N
    cnt = 0
    for j in range(N):
        if cnt < 0:
            break
        else:
            if (i >> j) & 1:
                kakko[j] = '1'
                cnt += 1
            else:
                kakko[j] = '0'
                cnt -= 1

    if cnt == 0:
        ans.append(int(''.join(kakko)))
    else:
        pass

ans.sort(reverse=True)

for k in ans:
    k = list(str(k))
    for l in range(len(k)):
        if k[l] == '1':
            k[l] = '('
        else:
            k[l] = ')'
    print(''.join(k))