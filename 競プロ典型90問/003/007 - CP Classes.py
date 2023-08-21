N = int(input())
A = sorted(list(map(int,input().split())))
Q = int(input())
B = []
for b in range(1,Q+1):
    B.append(int(input()))

def binary_search(data, value):
    left = 0
    mid = 0
    right = len(data) - 1
    while left <= right:
        mid = (left + right) // 2
        if data[mid] == value:
            return 0
        elif data[mid] < value:
            left = mid + 1
        else:
            right = mid - 1

    if mid == 0:
        if len(data) == 1:
            return abs(data[0]-value)
        else:
            return min(abs(data[0]-value),abs(data[1]-value))
    elif mid == len(data)-1:
        return min(abs(data[-1]-value),abs(data[-2]-value))
    else:
        return min(
            min(abs(data[mid-1]-value),abs(data[mid]-value)),
            min(abs(data[mid]-value),abs(data[mid+1]-value))
        )

for b in B:
    print(binary_search(A,b))