from math import sqrt
def chia3(n):
    if n % 3 == 0: return True
    else: return False
for test in range(int(input())):
    print('YES') if chia3(sum(int(i) for i in input())) else print('NO')