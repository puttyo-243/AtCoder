def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    r = [None] * n
    for i in range(0, n-1):
        if i == 0:
            r[i] = 0
        else:
            r[i] = r[i-1]

        while r[i] < n-1 and a[r[i]+1] - a[i] <= k:
            r[i] += 1
    
    ans = 0
    for i in range(0, n-1):
        ans += (r[i] - i)
    
    return ans


if __name__ == '__main__':
    print(main())