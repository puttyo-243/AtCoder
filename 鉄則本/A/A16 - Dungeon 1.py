def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    dp = [None] * (n + 1)

    for i in range(n + 1):
        if i == 0 or i == 1:
            a.insert(i,0)
            b.insert(i,0)
            dp[i] = 0
        elif i == 2:
            b.insert(i,0)
            dp[i] = a[2]
        else:
            dp[i] = min(dp[i-1] + a[i], dp[i-2] + b[i])

    print(dp[n])
    return

if __name__ == '__main__':
    main()