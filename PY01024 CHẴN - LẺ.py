def isValid (n):
    for i in range(1, len(n)):
        if abs(int(n[i]) - int(n[i-1])) != 2:
            return False
    return True

for test in range(int(input())):
    n = input()
    print ("YES" if not (sum(int(i) for i in n) % 10) and isValid(n) else "NO")