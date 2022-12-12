for test in range(int(input())):
    s1 = sorted(input())
    s2 = sorted(input())
    print(f'Test {test + 1}: ', end = '')
    print('YES' if s1 == s2 else 'NO')