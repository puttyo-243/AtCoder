def main():
    n = int(input())
    h = list(map(int, input().split()))

    h.insert(0,0)
    dp = [None] * (n+1)

    for i in range(n+1):
        if i == 0 or i == 1:
            dp[0] = 0
            dp[1] = 0
        elif i == 2:
            dp[2] = abs(h[2] - h[1])
        else:
            dp[i] = min(dp[i-1] + abs(h[i-1] - h[i]), dp[i-2] + abs(h[i-2] - h[i]))

    print(dp[n])
    return

if __name__ == '__main__':
    main()