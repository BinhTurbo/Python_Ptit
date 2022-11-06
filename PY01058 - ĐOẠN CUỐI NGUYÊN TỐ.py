import math


def isPrime(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return n > 1
for test in range(int(input())):
    n = input()
    temp = n[len(n) - 4:]
    print('YES') if isPrime(int(temp)) else print('NO')