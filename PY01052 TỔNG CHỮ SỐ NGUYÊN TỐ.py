from math import sqrt
def isPrime(n):
    for i in range(2, (int)(sqrt(n) + 1)):
        if n % i == 0: return False
    return n > 1
for test in range(int(input())):
    print('YES') if isPrime(sum(int(i) for i in input())) else print('NO')