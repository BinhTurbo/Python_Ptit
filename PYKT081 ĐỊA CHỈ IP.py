def check(s) :
    if len(s) < 4 : return False
    for i in s :
        if i.isdigit():
            if int(i) < 0 or int(i) > 255 : return False
        else: return False
    return True
for test in range(int(input())) :
    a = input().split('.')
    print("YES") if check(a) else print("NO")