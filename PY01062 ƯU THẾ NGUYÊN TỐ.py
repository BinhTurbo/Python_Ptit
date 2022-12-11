import math


def isPrime(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return n > 1
def procedure(n):
    nt = 0
    knt = 0
    for i in range(len(n)):
        if isPrime(int(n[i])):
            nt += 1
        else:
            knt += 1
    if isPrime(len(n)) and nt > knt:
        print("YES")
    else:
        print("NO")
for test in range(int(input())):
    procedure(input())