def sum(n):
    s = 0
    for i in n:
        s += ord(i) - ord('0')
    return str(s)
n = input()
d = 0
while len(n) > 1:
    n = sum(n)
    d += 1
print(d) if d != 0 else print(1)