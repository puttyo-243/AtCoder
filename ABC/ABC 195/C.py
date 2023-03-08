N = int(input())

comma = 0
if N < 1000:
    print(0)
else:#Nの桁数に応じて1回のカンマの数が増える
    a = N - 999#カンマが何個付くか判定しないといけない数値の数　例)N=1003の場合n=4になる。1000,1001,1002,1003の4つを判定する。
    N_len = len(str(N))#最大の桁数
    if N_len == 4:
        comma += a
    else:
        for n in range(5, N_len + 1):#最大桁数分繰り返す
            before_one_digit = ((1*10**(n-1)) - 1)
            comma += ((N - before_one_digit) * (n//3)) + ((before_one_digit - 999) * ((n-1)//3))

print(comma)
#4桁の数は9999‐999で9000個 9*10**(4-1)
#5桁の数は99999‐9999で90000個
# 6keta:2 5keta:90000 4keta:9000