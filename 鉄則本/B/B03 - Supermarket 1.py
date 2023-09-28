n = int(input())
a_list = list(map(int,input().split()))

ans = 'No'
for x in a_list:
    aa_list = list(set(a_list) - set([x]))
    for y in aa_list:
        aaa_list = list(set(aa_list) - set([y]))
        for z in aaa_list:
            if (x != y != z) and (x + y + z == 1000):
                ans = 'Yes'

print(ans)