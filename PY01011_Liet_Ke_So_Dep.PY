T = ['1', '3', '5', '7', '9']
def procedure(s):
    for i in s:
        if i in T:
            return ''
    return s + s[::-1] + ' '
        
test = int(input())
while test > 0:
    n = int(input())
    i = 1
    while True:
        s = str(i)
        if int(s + s[::-1]) >= n:
            break
        i += 1
        print(procedure(s), end="")   
    print()
    test -= 1
    