def check():
    s = input()
    return True if (s[-2: ] == '86') else False
#
for test in range(int(input())):
    print("YES" if check() else "NO")