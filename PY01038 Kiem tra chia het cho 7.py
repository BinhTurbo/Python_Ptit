for test in range(int(input())):
    n = input()
    kt = True
    for i in range(1000):
        if int(n) % 7 == 0:
            print(n)
            kt = False
            break
        else:
            n = str(int(n) + int(n[::-1]))
    if kt == True: print(-1)