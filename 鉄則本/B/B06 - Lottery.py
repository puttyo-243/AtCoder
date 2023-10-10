n = int(input())
a_list = list(map(int,input().split()))
q = int(input())
questions = []
for _ in range(1,q+1):
    questions.append(list(map(int,input().split())))

win_list = [0] * (n + 1)
lose_list = [0] * (n + 1)

cnt = 1
for a in a_list:
    if a == 0:
        lose_list[cnt] = lose_list[cnt-1] + 1
        win_list[cnt] = win_list[cnt-1]
    elif a == 1:
        lose_list[cnt] = lose_list[cnt-1]
        win_list[cnt] = win_list[cnt-1] + 1
    cnt += 1

for l,r in questions:
    if (win_list[r] - win_list[l-1]) > (lose_list[r] - lose_list[l-1]):
        print('win')
    elif (win_list[r] - win_list[l-1]) == (lose_list[r] - lose_list[l-1]):
        print('draw')
    else:
        print('lose')