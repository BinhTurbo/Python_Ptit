import math


def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n) + 1)):
        if n % i == 0:
            return False
    return True

test = int(input())
while test > 0:
    a, b = [int(i) for i in input().split()]
    print("YES" if isPrime(sum(int(i) for i in str(math.gcd(a,b)))) else "NO")
    test -= 1