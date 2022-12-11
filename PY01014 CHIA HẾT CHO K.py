a, k, n = [int(i) for i in input().split()]

if int(a / k) < int(n / k):
    for i in range(int(a/k) + 1, int(n / k) + 1):
        print(k * i - a, end = ' ')
else: 
    print(-1)