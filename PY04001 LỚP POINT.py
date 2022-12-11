from math import sqrt
class Point:
    def __init__(self, p1, p2):
        self.x = p1
        self.y = p2
    def distance(self, other):
        return '{:.4f}'.format(sqrt(pow(self.x - other.x, 2) + pow(self.y - other.y, 2)))

def Decimal(x):
    return float(x)

if __name__ == '__main__':
    test = int(input())
    while test > 0:
        A = input().split()
        p1 = Point(Decimal(A[0]), Decimal(A[1]))
        p2 = Point(Decimal(A[2]), Decimal(A[3]))
        print(p1.distance(p2))
        test -= 1