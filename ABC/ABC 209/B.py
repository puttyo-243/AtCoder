N,X = map(int,input().split())
A = list(map(int,input().split()))

teika = 0
for a in A:
    teika += a

if len(A)%2 == 0:
    teika -= len(A)/2
else:
    teika -= ((len(A)-1)/2)

if X >= teika:
    print("Yes")
else:
    print("No")