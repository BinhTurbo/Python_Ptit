import math

def isprime(n):
    if n < 2:
        return False
    r = int(math.sqrt(n))+1
    for i in range(2, r):
        if n%i != 0:
            return False
    return True

for t in range(int(input())):
    num = int(input())
    count = 0
    for i in range(1, num):
        if math.gcd(i, num) == 1:
            count += 1
    print("YES" if isprime(count) else "NO")