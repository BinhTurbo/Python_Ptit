import math


def isPrime(n):
    for i in range(2, int(math.sqrt(n) + 1)):
        if n % i == 0: return False
    return n > 1
for test in range(int(input())):
    n = input()
    t1 = n[:3]
    t2 = n[len(n) - 3:]
    print('YES') if len(n) >= 4 and isPrime(int(t1)) and isPrime(int(t2)) else print('NO')
    
    