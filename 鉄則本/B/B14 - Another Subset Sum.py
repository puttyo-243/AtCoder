def check(x, li):
    l = 0
    r = len(li) - 1
    while l <= r:
        m = (l + r) // 2
        if x < li[m]:
            r = m - 1
        elif x == li[m]:
            return True
        elif li[m] < x:
            l = m + 1
    return False

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a_left = a[:(len(a)//2)]
    a_right = a[(len(a)//2):]

    p = []
    for i in range(n+1):
        for comb in itertools.combinations(a_left, i):
            p.append(sum(comb))

    q = []
    for i in range(n+1):
        for comb in itertools.combinations(a_right, i):
            q.append(sum(comb))

    q.sort()

    ans = 'No'
    if len(a) == 1:
        if a[0] == k:
            ans = 'Yes'
    else:
        for i in p:
            result = check(k-i, q)
            if result == True:
                ans = 'Yes'
            else:
                pass

    return ans

if __name__ == '__main__':
    import itertools
    print(main())