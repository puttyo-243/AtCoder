def sum(z, left, right):
    return z[right+1] - z[left]

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    z = [0] * (n+1)
    for i in range(1, n+1):
        z[i] = a[i-1] + z[i-1]

    r = [0] * n
    for i in range(n):
        if i == 0:
            r[i] = -1
        else:
            r[i] = r[i-1]
        
        while r[i] < n-1 and sum(z, i, r[i] + 1) <= k:
            r[i] += 1
    
    ans = 0
    for i in range(n):
        ans += (r[i] - i + 1)
    
    return ans



if __name__ == '__main__':
    print(main())