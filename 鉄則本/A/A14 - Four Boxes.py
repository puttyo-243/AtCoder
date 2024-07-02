def check(x, q):
    l = 0
    r = len(q) - 1
    while l < r:
        m = (l+r)//2
        if x < q[m]:
            r = m - 1
        elif x == q[m]:
            return True
        elif q[m] < x:
            l = m + 1

    return False

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))
    d = list(map(int, input().split()))

    p = []
    for i in range(n):
        for j in range(n):
            p.append(a[i] + b[j])

    q = []
    for i in range(n):
        for j in range(n):
            q.append(c[i] + d[j])

    p.sort()
    q.sort()

    ans = 'No'
    for i in p:
        result = check(k-i, q)
        if result == True:
            ans = 'Yes'
            break
        else:
            pass

    return ans

if __name__ == '__main__':
    print(main())