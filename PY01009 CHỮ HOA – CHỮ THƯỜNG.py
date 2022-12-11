s = input()
def procedure():
    up, low = 0, 0
    for i in s:
        if i >= 'A' and i <= 'Z':
            up += 1
        elif i >= 'a' and i <= 'z':
            low += 1
    return 1 if up > low else 0
print(s.upper() if procedure() == 1 else s.lower())