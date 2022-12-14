from math import sqrt
def isPrime(n):
    for i in range(3, int(sqrt(n)) + 1, 2):
        if n % i == 0: return False
    return n == 2 or (n > 2 and n % 2 != 0)
n, m = [int(i) for i in input().split()]
a = []
np = []
for i in range(n):
    a += [[int(j) for j in input().split()]]
for i in range(n):
    tmp = []
    for j in range(m):
        if isPrime(a[i][j]):
            tmp.append(1)
        else:
            tmp.append(0)
    np += [tmp]
for i in range(n):
    for j in range(m):
        print(np[i][j], end = ' ')
    print()