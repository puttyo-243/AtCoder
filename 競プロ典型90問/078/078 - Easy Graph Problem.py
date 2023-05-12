N,M = map(int,input().split())

adjacency_list = [0] * N
for i in range(M):
    a,b = map(int,input().split())
    if a < b:
        adjacency_list[b-1] += 1
    else:
        adjacency_list[a-1] += 1

print(adjacency_list.count(1))

'''N,M = map(int,input().split())
A = []

for i in range(1,M+1):
    A.append(list(map(int,input().split())))

vertex_conn = {}
for a,b in A:
    vertex_conn.setdefault(a,[]).append(b)
    vertex_conn.setdefault(b,[]).append(a)

def find_index(lst, value):
    index = 0
    while index < len(lst) and lst[index] < value:
        index += 1
    return index

ans = 0
for key,value in vertex_conn.items():
    sorted(value)
    a = find_index(sorted(value),key)
    if a == 0:
        pass
    elif a == 1:
        ans += 1
    else:
        pass

print(ans)'''