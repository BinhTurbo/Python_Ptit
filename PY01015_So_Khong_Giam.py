def check(s):
    for i in range(0,len(s) - 1):
        if s[i] > s[i + 1]:
            return False
    return True
test = int(input())
while test > 0:
    s = input()
    print("YES") if check(s) else print("NO")
    test -= 1
    