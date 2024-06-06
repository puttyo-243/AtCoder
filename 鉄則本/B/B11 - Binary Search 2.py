import bisect

# 入力
n = int(input())
a_ = list(map(int, input().split()))
q = int(input())
x_list = []
for _ in range(q):
    x_list.append(int(input()))

# 処理
a = sorted(a_)

def find_lt(x):   # 探索したい数値未満のうち最大の数値を探索
    'Find rightmost value less than x'
    i = bisect.bisect_left(a, x)
    if i:
        return i
    else:
        return 0

# 出力
for x in x_list:
    print(find_lt(x))