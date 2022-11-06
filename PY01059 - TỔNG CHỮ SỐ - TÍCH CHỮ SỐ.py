def procedure(n):
    sum = 0
    tich = 1
    has = True
    for index, value in enumerate(n):
        if not index % 2:
            sum += int(value)
        else:
            if int(value):
                has = False
                tich *= int(value)
    if has:
        tich = 0
    print(sum, tich, sep= " ")
for test in range(int(input())):
    procedure(input())