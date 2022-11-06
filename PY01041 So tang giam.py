def isValid (n):
    if len(n) < 3:
        return False
    i = 1
    while i < len(n) and n[i] > n[i-1]:
        i += 1
    while i < len(n) and n[i] < n[i-1]:
        i += 1
    return i == len(n)

for test in range(int(input())):
    s = input()
    print("YES" if isValid(s) else "NO")