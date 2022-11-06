import math


for test in range(int(input())):
    n = input()
    m = n[::-1]
    n = int(n)
    m = int(m)
    if math.gcd(n,m) != 1:
        print('NO')
    else:
        print('YES')