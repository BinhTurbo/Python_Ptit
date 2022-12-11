def check(A, B):
    for i in range(len(A)):
        if A[i] > B[i]:
            return False
    return True

test = int(input())
while (test > 0):
    n = int(input())
    A = sorted([int(i) for i in input().split()])
    B = sorted([int(i) for i in input().split()])
    print("YES" if check(A, B) else "NO")
    test -= 1