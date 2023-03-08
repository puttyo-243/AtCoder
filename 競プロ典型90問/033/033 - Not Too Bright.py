import math

input_list = list(map(int,input().split()))
H = input_list[0]
W = input_list[1]


if H>1 and W>1:
    print((math.ceil(H/2)) * (math.ceil(W/2)))
else:
    print(H * W)