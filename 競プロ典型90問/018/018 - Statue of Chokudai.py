import math

t = int(input())
l,x,y = map(int,input().split())
q = int(input())
e_list = []
for _ in range(q):
    e_list.append(int(input()))

for e in e_list:
    # 直角三角形の底辺をa、高さをb、斜辺をcとする
    a = x - (e/t)*(l*2)
    b = (e/t)*(l*2)

    theta = math.degrees(math.atan2(b,a))
    