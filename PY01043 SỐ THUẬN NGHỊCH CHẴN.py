def check_thuan_nghich(n):
    for i in range(int(len(n) / 2) + 1):
        if n[i] != n[len(n) - i - 1]:
            return False
    return True
def check_chu_so_chan(n):
    for i in range(len(n)):
        if int(n[i]) % 2 != 0:
            return False
    return True
def check_len(n):
    if len(n) % 2 == 0: return True
    else: return False
for test in range(int(input())):
    t = int(input())
    for i in range(22, t, 2):
        if check_thuan_nghich(str(i)) and check_chu_so_chan(str(i)) and check_len(str(i)):
            print(i,end=' ')
    print()