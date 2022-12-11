P = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_."
while True:
    s = input()
    if s.strip() == '0':
        break
    k, s = s.split()
    k = int(k)
    temp = ''
    for i in s:
        temp += P[(P.index(i) + k) % 28]
    print(temp[::-1])