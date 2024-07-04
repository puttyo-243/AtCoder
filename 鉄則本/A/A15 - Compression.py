def check(x, li):
    l = 0
    r = len(li) - 1
    while l <= r:
        m = (l + r) // 2
        if x < li[m]:
            r = m - 1
        elif x == li[m]:
            return m + 1
        elif li[m] < x:
            l = m + 1

def main():
    n = int(input())
    a = list(map(int, input().split()))

    a_ = list(set(sorted(a)))
    a_.sort()

    b = []
    for i in range(n):
        b.append(check(a[i], a_))

    for i in range(len(b)):
        print(b[i],end=' ')

    return 

if __name__ == '__main__':
    main()