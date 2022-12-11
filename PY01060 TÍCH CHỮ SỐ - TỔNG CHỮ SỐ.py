def procedure(n):
    sum = 0
    tich = 1
    for index, value in enumerate(n):
        if not index % 2 and int(value) != 0:
            tich *= int(value)
        else:
            sum += int(value)
    print(tich, sum, sep= " ")
for test in range(int(input())):
    procedure(input())