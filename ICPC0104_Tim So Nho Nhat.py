for test in range(int(input())):
    s = input() + 'a'
    num_min = 10 ** 20
    temp = 0
    for i in range(len(s)):
        if s[i].isnumeric():
            temp = temp * 10 + int(s[i])
        elif s[i].isalpha() and s[i - 1].isnumeric():
            num_min = min(temp, num_min)
            temp = 0
    print(num_min)
    
    