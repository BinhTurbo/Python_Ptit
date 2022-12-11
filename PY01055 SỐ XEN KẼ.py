def check(n):
    if len(n) % 2 == 0: return False
    if n[0] == n[1]: return False
    for i in range(0,len(n) - 2,2):
        if n[i] != n[i + 2]:
            return False
    return True
for test in range(int(input())):
    n = input()
    print('YES') if check(n) else print('NO')