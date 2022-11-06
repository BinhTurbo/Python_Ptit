def check(n):
    sum = 0
    for i in range(len(n)):
        sum += int(n[i])
    temp = str(sum)
    if temp == temp[::-1] and len(temp) > 1: return True
    else: return False
for test in range(int(input())):
    n = input()
    print('YES') if check(n) else print('NO')