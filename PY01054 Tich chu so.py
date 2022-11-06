def multi(n):
    tich = 1
    for i in range(len(n)):
        if n[i] == '0': continue
        else:
            tich *= int(n[i])
    return tich
for test in range(int(input())):
    s = input()
    print(multi(s))