n = int(input())

def f(x):
    return x**3 + x

l = 0.0
r = 100.0
for _ in range(20):
    m = (l+r)/2
    val = f(m)
    if val > n:
        r = m
    else:
        l = m
print(m)