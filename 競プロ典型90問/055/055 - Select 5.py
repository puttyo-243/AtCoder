from itertools import combinations as comb

N, P, Q = map(int,input().split())
A_list = list(map(int,input().split()))

A = comb(A_list,5)
dict_ans = {}
for a in list(A):
    prod = 1
    for i in a:
        prod *= i
    
    if prod % P == Q:
        print(a)
        try:
            dict_ans[prod] +=1
        except KeyError:
            dict_ans[prod] = 0
            dict_ans[prod] +=1

ans = sum(dict_ans.values())

print(ans)

