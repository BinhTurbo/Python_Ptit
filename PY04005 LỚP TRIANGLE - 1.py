from math import sqrt

class Point:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        
class Triangle:
    def __init__(self, p1, p2, p3):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
        
    def distance(self, p1, p2):
        return sqrt((p1.a - p2.a) ** 2 + (p1.b - p2.b) ** 2)
    
    def sum(self):
        a = self.distance(self.p1, self.p2)
        b = self.distance(self.p1, self.p3)
        c = self.distance(self.p2, self.p3)
        if max(a, b, c) * 2 >= a+b+c:
            return 'INVALID'
        return '{:.3f}'.format(a+b+c)

A = []
test = int(input())
for _ in range(test):
    A += [float(i) for i in input().split()]
i = 0
for index in range(test):
    print(Triangle(Point(A[i], A[i+1]), Point(A[i+2], A[i+3]), Point(A[i+4], A[i+5])).sum())
    i += 6