n, m = input().split()
n, m = int(n), int(m)

move_i = [-1, -1, -1, 0, 0, 1, 1, 1]
move_j = [-1, 0, 1, -1, 1, -1, 0, 1]

cnt = 0
mat = [[0 for y in range(m+2)] for x in range(n+2)]
for i in range(1, n+1):
    arr = [int(x) for x in input().split()] 
    for j in range(1, m+1):
        mat[i][j] = arr[j-1]

vis = [[False for y in range(m+2)] for x in range(n+2)]

sum = 0
for i in range(1, n+1):
    for j in range(1, m+1):
        if mat[i][j] == -1:
            for k in range(8):
                new_i, new_j = i+move_i[k], j+move_j[k]
                if vis[new_i][new_j] == False:
                    sum += mat[new_i][new_j]
                    vis[new_i][new_j] = True

print(sum)