from math import sqrt
def isPrime (n):
    for i in range (2, (int)(sqrt(n) + 1)):
        if not n%i:
            return False
    return n > 1
def check(s):
    if isPrime(int(len(s))) == False: return False
    Prime = 0
    NoPrime = 0
    for i in s:
        if isPrime(int(i)): Prime += 1
        else: NoPrime += 1
    return True if Prime > NoPrime else  False
for test in range(int(input())):
    n = input()
    print('YES') if check(n) else print('NO')
    