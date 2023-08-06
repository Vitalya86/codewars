n = int(input())

matrix = []
flag = True
for _ in range(n):
    temp = [int(i) for i in input().split()]
    matrix.append(temp)
for i in range(n):
    for j in range(n):
        if matrix[i][j] != matrix[j][i] and i != j:
            flag = False
if flag:
    print('YES')
else:
    print('NO')
