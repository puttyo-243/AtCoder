N,K = map(int,input().split())

li_9 = []
def change_to_base9(n):
    if (n // 9) >= 9:
        li_9.append(str(n % 9))
        return change_to_base9(n // 9)
    else:
        li_9.append(str(n % 9))
        li_9.append(str(n // 9))
        li_return = li_9.copy()
        li_9.clear()
        return li_return[::-1]

def eight_five(n):
    li_5 = []
    for i in str(n):
        if i == '8':
            li_5.append('5')
        else:
            li_5.append(i)
    return int("".join(li_5))

a=0
for k in range(1,K+1):
    if k == 1:
        a = eight_five(int("".join(change_to_base9(int(str(N),8)))))
    else:
        a = eight_five(int("".join(change_to_base9(int(str(a),8)))))


print(a)