X = ['0','1','2']
def check(s):
    for i in s:
        if not i in X:
            return False
    return True
for test in range(int(input())):
    s = input()
    print("YES") if check(s) == True else print("NO")