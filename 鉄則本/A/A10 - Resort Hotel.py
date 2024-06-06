# 入力
n = int(input())
a = list(map(int, input().split()))
d = int(input())
l = [None] * d
r = [None] * d
for i in range(d):
    l[i], r[i] = map(int, input().split())

# 処理 累積和ではなく累積maxを使う
p = [0] * n
q = [0] * n

p[0] = a[0]
for i in range(1,n):
    p[i] = max(p[i-1],a[i])

q[-1] = a[-1]
for i in range(n-2,-1,-1):
    q[i] = max(q[i+1],a[i])


# 出力
for i in range(d):
    print(max(p[(l[i]-1)-1],q[(r[i]+1)-1]))
"""
入力
7
1 2 5 5 2 3 1
2
3 5
4 6

両側から累積maxを求める
右からの累積和はappendではなくinsert
p = [0] * n
q = [0] * n
[1,2,5,5,5,5,5] [5,5,5,5,3,3,1]
左リストは左から(L-1)番目、右リストは左から(R+1)番目の値でmax()

L=3,R=5の場合
max(2,3)=3
L=4,R=6の場合
max(5,3)=5
出力
3
5
"""