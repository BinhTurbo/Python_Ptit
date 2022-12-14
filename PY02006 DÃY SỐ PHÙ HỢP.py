def checkArray(A, B):
    for i in range(len(A)):
        if A[i] > B[i]:
            return False
    return True
for test in range(int(input())):
    n = int(input())
    A = [int(i) for i in input().split()]
    A.sort()
    B = [int(i) for i in input().split()]
    B.sort()
    print("YES" if checkArray(A, B) else "NO")