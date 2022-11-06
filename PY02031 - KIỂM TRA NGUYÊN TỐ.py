import math


def isPrime(n):
    for i in range(2, int (math.sqrt(n)) + 1):
        if n % i == 0: return False
    return n > 1
n, m = [int(x) for x in input().split()]
for i in range(n):
    a = [int(x) for x in input().split()]
    for i in a:
        if isPrime(i): 
            print(1, end=' ')
        else:
            print(0, end=' ')
    print()