test = int(input())
while test > 0:
    s = input()
    t1 = s[:2]
    t2 = s[len(s) - 2:]
    if t1 == t2:
        print("YES")
    else:
        print("NO")
    test -= 1