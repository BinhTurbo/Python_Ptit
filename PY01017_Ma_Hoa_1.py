from itertools import count


test = int(input())
for t in range(0,test):
    s = input() + ' '
    cnt = 0
    c = s[0]
    temp = ''
    for i in s:
        if i == c:
            cnt += 1
        else:
            temp += str(cnt) + c
            c = i
            cnt = 1
    print(temp)