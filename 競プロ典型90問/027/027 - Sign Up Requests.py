N = int(input())
S = {}
cnt = 1
for i in range(1,N+1):
    s = input()
    try:
        S[s]
    except KeyError:
        S[s] = cnt
    else:
        pass
    cnt += 1

registrant_list = []
date_count = 1
for k,v in S.items():
    print(v)
