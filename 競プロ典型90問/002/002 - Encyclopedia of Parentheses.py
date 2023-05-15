n = int(input())

def generateParenthesis(n):
    stack = [("(", 1, 0)]
    result = []
    while stack:
        s, left, right = stack.pop()
        if left == n and right == n:
            result.append(s)
        if left < n:
            stack.append((s + "(", left + 1, right))
        if right < left:
            stack.append((s + ")", left, right + 1))
    return result

print(generateParenthesis(n))

'''n = int(input())

for i in range(2**n):
    s = ""
    cnt = 0
    for j in range(n):
        if (i >> j) & 1:
            s += "("
            cnt += 1
        else:
            s += ")"
            cnt -= 1
        if cnt < 0:
            break
    if cnt == 0:
        print(s)'''

'''N = int(input())
cnt=0
li = ['(',')']# * (N//2) + [] * (N//2)
ans = []
for i in range(2**N):
    parentheses = []
    for j in range(N):
        if (i >> j) & 1:
            parentheses.insert(0,'1')
            #print('bin:'+str(bin(i))[2:].zfill(4)+' i:'+str(i),' j:'+str(j))
        else:
            parentheses.insert(0,'0')
    print(parentheses)
    #条件判定
    #半分にして右側の順番をひっくり返したものと左側比較して同じならansに追加
    left = parentheses[:N//2]
    right = parentheses[N//2:]

    reverse_right = right[::-1]
    for i in range(len(reverse_right)):
        if reverse_right[i] == '0':
            reverse_right[i] = '1'
        else:
            reverse_right[i] = '0'

    if left == reverse_right and left != right:
        ans.append(parentheses)
print(ans)'''