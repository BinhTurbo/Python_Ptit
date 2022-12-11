from math import gcd

class PhanSo:
    def __init__(self, x = None, y = None):
        self.x = x
        self.y = y
        
    def rutgon(self):
        tmp = gcd(self.x, self.y)
        self.x //= tmp
        self.y //= tmp
        
    def __add__(self, other):
        P = PhanSo()
        P.y = self.y * other.y
        P.x = self.x * other.y + self.y * other.x
        P.rutgon()
        return P
    
    def __str__(self) -> str:
        return f'{self.x}/{self.y}'
    
ip = [int(i) for i in input().split()]
P1 = PhanSo(ip[0], ip[1])
P2 = PhanSo(ip[2], ip[3])
P = P1 + P2
print(P)