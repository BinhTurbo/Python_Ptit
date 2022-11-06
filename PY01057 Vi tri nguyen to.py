import math

PRIME = '2357'
def isPrime(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0: return False
    return n > 1
def check(n):
    for i in range(len(n)):
        if isPrime(i) and n[i] not in PRIME or not isPrime(i) and n[i] in PRIME:
            return 'NO'
    return 'YES'
for test in range(int(input())):
    n = input()
    print(check(n))
    