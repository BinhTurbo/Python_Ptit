import math


def isPrime(n):
    for i in range(2, int(math.sqrt(n) + 1)):
        if n % i == 0:
            return False
    return n > 1
def check(n):
    for i in range(1, len(n), 2):
        if int(n[i]) % 2 == 0: return False
    for i in range(0, len(n), 2):
        if int(n[i]) % 2 != 0: return False
    s = sum(int(i) for i in n)
    if isPrime(s): return True
    return False
for test in range(int(input())):
    n = input()
    print('YES') if check(n) else print('NO')

